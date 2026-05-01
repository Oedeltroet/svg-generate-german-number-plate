area_code = "GO"
serial_letters = "XY"
serial_digits = "123"

import math, svg

def star_points(cx, cy, r_outer, r_inner, rotation_deg = -90):
    
	points = []

	for i in range(10):
    
		angle = math.radians(rotation_deg + i * 36)
		radius = r_outer if i % 2 == 0 else r_inner

		x = cx + math.cos(angle) * radius
		y = cy + math.sin(angle) * radius

		points.append(f"{x:.3f},{y:.3f}")

	return " ".join(points)

def add_star(parent, cx, cy, r_outer = 2.2):
    
	r_inner = r_outer * 0.381966

	parent.elements.append(
        svg.Polygon(
			points = star_points(cx, cy, r_outer, r_inner),
			fill = "#ffcc00",
			stroke = "none"
    	)
    )

def add_eu_stars(parent, center_x, center_y, circle_radius, star_radius = 2.2):
    
	for i in range(12):

		angle = math.radians(-90 + i * 30)

		cx = center_x + math.cos(angle) * circle_radius
		cy = center_y + math.sin(angle) * circle_radius

		add_star(parent, cx, cy, r_outer=star_radius)

canvas = svg.SVG(
	width = "520mm",
	height = "110mm",
	viewBox = svg.ViewBoxSpec(0, 0, 520, 110),
	elements = [
		# number plate background
		svg.Rect(
			x = "2.25",
			y = "2.25",
      		rx = "4.5",
			ry = "4.5",
        	width = "515.5",
        	height = "105.5",
			fill = "#ffffff"
		),
		# european country code area
        svg.Rect(
        	x = "4.5",
        	y = "4.5",
        	width = "40.5",
      		height = "101",
			fill = "#003399"
		),
		# number plate border
		svg.Rect(
			x = "2.25",
			y = "2.25",
      		rx = "4.5",
			ry = "4.5",
        	width = "515.5",
        	height = "105.5",
			fill = "none",
          	stroke = "#000000",
            stroke_width = "4.5",
            stroke_linejoin = "round",
            stroke_miterlimit = "4"
		)
    ],
)

add_eu_stars(
	canvas,
	center_x = 24.75,
	center_y = 43.5,
	circle_radius = 13.5,
	star_radius = 2.25
)

export_filename = f"{area_code}_{serial_letters}_{serial_digits}.svg"

with open(export_filename, "w") as f:
  f.write(canvas.as_str())