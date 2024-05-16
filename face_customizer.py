import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, PathPatch, Wedge, Rectangle
from matplotlib.path import Path

def draw_face(ax, features):
    # Draw face with color, size, and shape
    face_size = 0.4 * features['size']
    face_y_offset = 0.5 - (0.1 if features['shape'] == 'square' else 0)
    face = Wedge((0.5, face_y_offset), face_size, 0, 360, width=face_size * (0.8 if features['shape'] == 'round' else 0.6), color=features['color'], ec="black")
    ax.add_patch(face)

    # Draw eyes, gender influences size
    eye_size = 0.07 * features['size'] if features['gender'] == 'female' else 0.05 * features['size']
    left_eye = Circle((0.35, 0.65), eye_size, color='black')
    right_eye = Circle((0.65, 0.65), eye_size, color='black')
    ax.add_patch(left_eye)
    ax.add_patch(right_eye)

    # Draw eyebrows
    eyebrow_lift = 0.1 if features['eyebrows'] == 'raised' else 0
    ax.add_patch(Rectangle((0.28, 0.73 + eyebrow_lift), 0.14, 0.01, color='black'))
    ax.add_patch(Rectangle((0.58, 0.73 + eyebrow_lift), 0.14, 0.01, color='black'))

    # Draw mouth based on style
    mouth_y = 0.4 if features['shape'] == 'round' else 0.35
    mouth_y *= features['size']
    if features['mouth'] == 'smile':
        vertices = [(0.4, mouth_y), (0.5, mouth_y + 0.05), (0.6, mouth_y)]
    elif features['mouth'] == 'frown':
        vertices = [(0.4, mouth_y + 0.05), (0.5, mouth_y), (0.6, mouth_y + 0.05)]
    else:
        vertices = [(0.4, mouth_y), (0.6, mouth_y)]
    codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3] if features['mouth'] != 'neutral' else [Path.MOVETO, Path.LINETO]
    path = Path(vertices, codes)
    patch = PathPatch(path, fill=False, color='black')
    ax.add_patch(patch)

    # Draw nose based on gender
    nose_y = 0.55 if features['gender'] == 'female' else 0.53
    nose_path = Path([(0.5, nose_y), (0.49, 0.5), (0.51, 0.5)], [Path.MOVETO, Path.LINETO, Path.LINETO])
    nose_patch = PathPatch(nose_path, fill=False, color='black')
    ax.add_patch(nose_patch)

    # Draw beard if selected and gender is male
    if features['beard'] == 'yes' and features['gender'] == 'male':
        beard = Arc((0.5, 0.35), 0.25, 0.1, angle=0, theta1=180, theta2=360, color='black')
        ax.add_patch(beard)

    # Draw hair based on gender, style, and hair color
    hair_y = 0.85 if features['hair'] != 'none' else 0.85
    hair_height = 0.15 if features['hair'] == 'long' else 0.05
    if features['hair'] != 'none':
        ax.add_patch(Rectangle((0.35, hair_y), 0.3, hair_height, color=features['hair_color']))

def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    features = {
        'mouth': input("Choose mouth style (smile, neutral, frown): "),
        'nose': input("Choose nose type (standard, none): "),
        'color': input("Choose face color (yellow, peach, brown, white): "),
        'eyebrows': input("Choose eyebrow style (normal, raised): "),
        'shape': input("Choose face shape (round, square): "),
        'jaw': input("Choose jaw type (strong, weak): "),
        'beard': input("Does he have a beard? (yes, no): "),
        'gender': input("Choose gender (male, female): "),
        'hair': input("Choose hair type (none, short, long): "),
        'hair_color': input("Choose hair color (black, brown, blonde, red): "),
        'size': float(input("Choose face size (0.8 for smaller, 1.2 for larger, 1 for normal): "))
    }

    draw_face(ax, features)
    
    plt.show()

if __name__ == "__main__":
    main()
