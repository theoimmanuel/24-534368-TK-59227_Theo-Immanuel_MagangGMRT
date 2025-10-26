# Theo Immanuel S.
# 24/534368/TK/59227
# Forward Kinematics - GMRT Week 1

import numpy as np
import matplotlib.pyplot as plt

def forward_kinematics(t1, t2, L1, L2): # definisi fungsi FK
    # konversi theta (derajat) ke radian
    t1_rad = np.radians(t1)
    t2_rad = np.radians(t2)
    
    # posisi titik pusat
    x0, y0 = 0, 0

    # posisi titik elbow (joint 1)
    x1 = L1 * np.cos(t1_rad)
    y1 = L1 * np.sin(t1_rad)
    
    # posisi titik akhir (end effector)
    x_end = x1 + L2 * np.cos(t1_rad + t2_rad) # karena x0 = 0 --> lihat hasil perhitungan
    y_end = y1 + L2 * np.sin(t1_rad + t2_rad) # karena y0 = 0 --> lihat hasil perhitungan
    
    return x_end, y_end, (x1, y1)

def plot(t1, t2, L1, L2, x_end, y_end, joint1): # definisi fungsi plot
    # ukuran
    plt.figure(figsize=(10, 8))
    
    # garis penghubung
    plt.plot([0, joint1[0]], [0, joint1[1]], 'ro-', linewidth=3, markersize=5, label=f'(Femur = {L1})')
    plt.plot([joint1[0], x_end], [joint1[1], y_end], 'go-', linewidth=3, markersize=5, label=f'(Tibia = {L2})')
    
    # titik awal
    plt.plot(0, 0, 'bs', markersize=10, label='Base (0,0)')
    
    # titik end effector
    plt.plot(x_end, y_end, 'r*', markersize=10, label=f'End Effector ({x_end:.2f}, {y_end:.2f})')
    
    # garis sumbu
    plt.axhline(y=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    
    # label
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.xlabel('X (cm)', fontsize=12)
    plt.ylabel('Y (cm)', fontsize=12)
    plt.title(f'Forward Kinematics:', fontsize=14, fontweight='bold')
    plt.legend(loc='best', fontsize=10)
    
    plt.tight_layout()
    plt.show()

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
    x_end, y_end, joint1 = forward_kinematics(t1, t2, L1, L2)
    
    print(f"Base Position : (0.00, 0.00)")
    print(f"Elbow Position: ({joint1[0]:.2f}, {joint1[1]:.2f})")
    print(f"End Effector Position: ({x_end:.2f}, {y_end:.2f})")

    # plot visualisasi

    plot(t1, t2, L1, L2, x_end, y_end, joint1)

