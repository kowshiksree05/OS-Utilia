from flask import Flask, render_template, request, jsonify
import psutil
import os
# import pwd

app = Flask(__name__)

# Function to fetch system resources
def get_system_resources():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    cpu_freq = psutil.cpu_freq()
    return {
        'cpu_usage': cpu_usage,
        'cpu_freq':cpu_freq,
        'memory_usage': memory_info.percent,
        'total_memory': memory_info.total,
        'available_memory': memory_info.available,
        'disk_usage': disk_usage.percent,
        'total_disk': disk_usage.total,
        'used_disk': disk_usage.used,
        'free_disk': disk_usage.free
    }


# Function to fetch running processes with pagination
def get_processes(offset=0, limit=10):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_percent']):
        try:
            proc_info = proc.info
            processes.append({
                'pid': proc_info['pid'],
                'name': proc_info['name'],
                'status': proc_info['status'],
                'cpu_usage': proc_info['cpu_percent'],
                'memory_usage': proc_info['memory_percent'],
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return processes[offset:offset + limit]

# Function to get network connections
def get_network_connections():
    connected_devices = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr:  # Only include connections with a remote address
            connected_devices.append({
                'local_address': f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else 'N/A',
                'remote_address': f"{conn.raddr.ip}:{conn.raddr.port}",
                'status': conn.status
            })
    return connected_devices

# Function to get active users
def get_active_users():
    users = psutil.users()
    return [user.name for user in users]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/system_resources', methods=['GET'])
def system_resources():
    resources = get_system_resources()
    return jsonify(resources)

@app.route('/api/processes', methods=['GET'])
def processes():
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', 10))
    procs = get_processes(offset, limit)
    return jsonify(procs)

@app.route('/api/connections', methods=['GET'])
def connections():
    network_connections = get_network_connections()
    return jsonify(network_connections)

@app.route('/api/users', methods=['GET'])
def users():
    active_users = get_active_users()
    return jsonify({'users': active_users})

@app.route('/api/sensors', methods=['GET'])
def sensors():
    sensors_data = get_sensors()
    return jsonify(sensors_data)

@app.route('/api/disk_partitions', methods=['GET'])
def disk_partitions():
    partitions = get_disk_partitions()
    return jsonify(partitions)

@app.route('/api/disk_io_counters', methods=['GET'])
def disk_io_counters():
    counters = get_disk_io_counters()
    return jsonify(counters)

@app.route('/api/net_io_counters', methods=['GET'])
def net_io_counters():
    counters = get_net_io_counters()
    return jsonify(counters)

@app.route('/api/net_if_addrs', methods=['GET'])
def net_if_addrs():
    addrs = get_net_if_addrs()
    return jsonify(addrs)

if __name__ == '__main__':
    app.run(debug=True)

