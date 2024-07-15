from PIL import Image, ImageDraw
import numpy as np

def draw_triangle(draw, x, y, size, fill):
    half_size = size // 2
    points = [(x, y - half_size), (x - half_size, y + half_size), (x + half_size, y + half_size)]
    draw.polygon(points, fill=fill)

def draw_square(draw, x, y, size, fill):
    half_size = size // 2
    points = [(x - half_size, y - half_size), (x + half_size, y - half_size), 
              (x + half_size, y + half_size), (x - half_size, y + half_size)]
    draw.polygon(points, fill=fill)

def fill_with_shapes(image_path, shape, shape_size=10):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    np_image = np.array(image)

    new_image = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(new_image)

    for y in range(0, image.height, shape_size):
        for x in range(0, image.width, shape_size):
            r, g, b, a = np_image[y, x]
            fill = (r, g, b, a)
            if shape == 'triangle':
                draw_triangle(draw, x, y, shape_size, fill)
            elif shape == 'square':
                draw_square(draw, x, y, shape_size, fill)

    new_image = Image.alpha_composite(image, new_image)
    return new_image

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fill an image with shapes.")
    parser.add_argument("image_path", type=str, help="Path to the input image")
    parser.add_argument("output_path", type=str, help="Path to save the output image")
    parser.add_argument("--shape", type=str, choices=['triangle', 'square'], default='square', help="Shape to fill with")
    parser.add_argument("--shape_size", type=int, default=10, help="Size of the shape")
    
    args = parser.parse_args()

    result_image = fill_with_shapes(args.image_path, args.shape, args.shape_size)
    result_image.save(args.output_path)
    print(f"Image saved to {args.output_path}")
