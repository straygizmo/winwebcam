import cv2
import platform
import subprocess
import sys

def check_camera_permissions():
    """Check if we have camera permissions on Windows"""
    print("=== Camera Diagnostic Tool ===\n")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Python version: {sys.version}")
    print(f"OpenCV version: {cv2.__version__}")
    print()

def list_cameras_windows():
    """List available cameras on Windows using different methods"""
    print("=== Method 1: OpenCV VideoCapture Test ===")
    available_cameras = []
    
    for i in range(10):  # Check more indices
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"Camera {i}: Available (frame size: {frame.shape if frame is not None else 'Unknown'})")
                available_cameras.append(i)
            else:
                print(f"Camera {i}: Opened but cannot read frame")
            cap.release()
        else:
            print(f"Camera {i}: Not available")
    
    print(f"\nFound {len(available_cameras)} working cameras: {available_cameras}")
    print()
    
    # Try DirectShow backend specifically for Windows
    print("=== Method 2: DirectShow Backend ===")
    for i in range(5):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"DirectShow Camera {i}: Available")
                available_cameras.append(f"DS_{i}")
            cap.release()
        else:
            print(f"DirectShow Camera {i}: Not available")
    
    print()
    
    # Try to list cameras using Windows commands
    print("=== Method 3: Windows Device Manager ===")
    try:
        result = subprocess.run(['powershell', '-Command', 
                               'Get-PnpDevice -Class Camera | Select-Object FriendlyName, Status'], 
                               capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("Camera devices found:")
            print(result.stdout)
        else:
            print("Could not list camera devices via PowerShell")
    except Exception as e:
        print(f"Error running PowerShell command: {e}")
    
    return available_cameras

def test_camera_access(camera_index):
    """Test accessing a specific camera"""
    print(f"=== Testing Camera {camera_index} ===")
    
    # Try regular backend
    cap = cv2.VideoCapture(camera_index)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print(f"✓ Camera {camera_index} works with default backend")
            print(f"  Frame shape: {frame.shape}")
            print(f"  Frame type: {type(frame)}")
        else:
            print(f"✗ Camera {camera_index} opened but cannot read frame")
        cap.release()
    else:
        print(f"✗ Camera {camera_index} cannot be opened with default backend")
    
    # Try DirectShow backend
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print(f"✓ Camera {camera_index} works with DirectShow backend")
        else:
            print(f"✗ Camera {camera_index} opened with DirectShow but cannot read frame")
        cap.release()
    else:
        print(f"✗ Camera {camera_index} cannot be opened with DirectShow backend")

if __name__ == "__main__":
    check_camera_permissions()
    cameras = list_cameras_windows()
    
    if cameras:
        print(f"\n=== Testing First Available Camera ===")
        first_camera = cameras[0]
        if isinstance(first_camera, int):
            test_camera_access(first_camera)
    else:
        print("\n=== No cameras found ===")
        print("Possible solutions:")
        print("1. Check if camera is physically connected")
        print("2. Check Windows Privacy Settings:")
        print("   - Go to Settings > Privacy & Security > Camera")
        print("   - Make sure 'Camera access' is turned on")
        print("   - Make sure 'Let apps access your camera' is turned on")
        print("3. Check if another application is using the camera")
        print("4. Try restarting the computer")
        print("5. Update camera drivers")
