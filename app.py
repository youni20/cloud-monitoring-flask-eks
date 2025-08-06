from flask import Flask, jsonify, render_template
import psutil
import platform
import os

app = Flask(__name__)

# Configuration
CPU_THRESHOLD = 80  # Alert if CPU usage is above the %

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    try:
        # Get current system stats
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        
        # Let's skip disk usage for now to test if everything else works
        try:
            # Try different approaches for disk usage
            if platform.system() == "Windows":
                # Method 1: Use shutil (most compatible)
                import shutil
                total, used, free = shutil.disk_usage("C:")
                disk_percent = (used / total) * 100
            else:
                disk = psutil.disk_usage('/')
                disk_percent = disk.percent
        except Exception as disk_error:
            print(f"Disk usage error: {disk_error}")  # Debug print
            try:
                # Method 2: Try psutil with different path
                disk = psutil.disk_usage("C:")
                disk_percent = disk.percent
            except:
                # Method 3: Fallback - get available partitions
                try:
                    partitions = psutil.disk_partitions()
                    if partitions:
                        main_partition = partitions[0].mountpoint
                        disk = psutil.disk_usage(main_partition)
                        disk_percent = disk.percent
                    else:
                        disk_percent = 0
                except:
                    disk_percent = 0
        
        # Check if CPU usage is high
        high_cpu = cpu_percent > CPU_THRESHOLD
        
        return jsonify({
            "cpu_usage": round(cpu_percent, 1),
            "memory_usage": round(memory.percent, 1),
            "disk_usage": round(disk_percent, 1),
            "high_cpu_alert": high_cpu,
            "status": "WARNING" if high_cpu else "OK",
            "threshold": CPU_THRESHOLD
        })
    
    except Exception as e:
        # Return error information for debugging
        return jsonify({
            "error": str(e),
            "status": "ERROR"
        }), 500

@app.route('/api/cpu')
def get_cpu():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        high_cpu = cpu_percent > CPU_THRESHOLD
        
        return jsonify({
            "cpu_usage": round(cpu_percent, 1),
            "high_cpu_alert": high_cpu,
            "threshold": CPU_THRESHOLD
        })
    
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "ERROR"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)