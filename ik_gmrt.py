# Theo Immanuel S.
# 24/534368/TK/59227
# Inverse Kinematics - GMRT Week 1

import numpy as np
import matplotlib.pyplot as plt

def inverse_kinematics(x_end, y_end, L1, L2): # definisi fungsi IK
    
    # hitung sudut rotasi --> rumus dari PPT Materi Week 2
    t2 = np.arccos((x_end ** 2 + y_end ** 2 - L1 ** 2 - L2 ** 2)/(2 * L1 * L2))
    t1 = np.arctan(y_end/x_end) - np.arctan((L2 * np.sin(t2))/(L1 + L2 * np.cos(t2))) 
    
    return t1, t2

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
    plt.title(f'Inverse Kinematics: θ1={t1}°, θ2={t2}°', fontsize=14, fontweight='bold')
    plt.legend(loc='best', fontsize=10)

    # notasi sudut
    plt.text(10, 5, f'θ1 = {t1:.2f}°', fontsize=10, bbox=dict(facecolor='wheat', alpha=0.5))
    plt.text(joint1[0]+5, joint1[1]+5, f'θ2 = {t2:.2f}°', fontsize=10, bbox=dict(facecolor='lightgreen', alpha=0.5))
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # panjang lengan
    L1 = 68  # Femur --> NIU: 534368
    L2 = 27  # Tibia --> NIF: 59227
    
    print(f"Femur Length: {L1} cm")
    print(f"Tibia Length: {L2} cm")
    
    # titik elbow
    joint1 = (52.09, 43.71) 
    print(f"Elbow (52.09, 43.71)")
    
    # titik end effector
    x_end = 61.33
    y_end = 69.08
    
    print(f"End Effector (61.33, 69.08)")
    
    # kalkulasi forward kinematics
    t1, t2 = inverse_kinematics(x_end, y_end, L1, L2)
    
    # konversi radian ke derajat
    t1 = np.degrees(t1)
    t2 = np.degrees(t2)

    print(f"Base Position : (0.00, 0.00)")
    print(f"End Effector Position: ({x_end}, {y_end})")
    print(f"Obtained Angles:")
    print(f"Servo 1 Angle: {t1:.2f}°")
    print(f"Servo 2 Angle: {t2:.2f}°")

    # plot visualisasi
    plot(t1, t2, L1, L2, x_end, y_end, joint1)