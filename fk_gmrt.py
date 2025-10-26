# Theo Immanuel S.
# 24/534368/TK/59227
# Forward Kinematics - GMRT Week 1

import numpy as np

def forward_kinematics(t1, t2, L1, L2): # definisi fungsi FK
    # konversi theta (derajat) ke radian
    t1_rad = np.radians(t1)
    t2_rad = np.radians(t2)
    
    # posisi titik pusat
    x0, y0 = 0, 0
    
    # posisi titik akhir (end effector)
    x_end = L1 * np.cos(t1_rad) + L2 * np.cos(t1_rad + t2_rad) # karena x0 = 0 --> lihat hasil perhitungan
    y_end = L1 * np.sin(t1_rad) + L2 * np.sin(t1_rad + t2_rad) # karena y0 = 0 --> lihat hasil perhitungan
    
    return x_end, y_end

if __name__ == "__main__":
    # panjang lengan
    L1 = 68  # Femur --> NIU: 534368
    L2 = 27  # Tibia --> NIF: 59227
    
    print(f"Femur Length: {L1} cm")
    print(f"Tibia Length: {L2} cm")
    
    # sudut rotasi
    t1 = 40  # counter-clockwise --> positive
    t2 = 30  # counter-clockwise --> positive
    
    print(f"Servo 1 Angle: {t1}°")
    print(f"Servo 2 Angle: {t2}°")
    
    # kalkulasi forward kinematics
    x_end, y_end = forward_kinematics(t1, t2, L1, L2)
    
    print(f"Base Position : (0.00, 0.00)")
    print(f"End Effector Position: ({x_end:.2f}, {y_end:.2f})")