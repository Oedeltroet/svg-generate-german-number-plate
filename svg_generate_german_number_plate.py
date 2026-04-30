area_code = "GO"
serial_letters = "XY"
serial_digits = "123"

import svg

canvas = svg.SVG(
	width = "520mm",
	height = "110mm",
	viewBox = "0 0 520 110",
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
		# european country code
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

export_filename = f"{area_code}_{serial_letters}_{serial_digits}.svg"

with open(export_filename, "w") as f:
  f.write(canvas.as_str())