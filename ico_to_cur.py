import argparse

def ico_to_cur(ico_path, cur_path, hotspot_x, hotspot_y):
    with open(ico_path, "rb") as f:
        ico_data = f.read()

    cur_data = bytearray(ico_data)

    # Write hotspot (little-endian 16-bit)
    cur_data[10] = hotspot_x & 0xFF
    cur_data[11] = (hotspot_x >> 8) & 0xFF
    cur_data[12] = hotspot_y & 0xFF
    cur_data[13] = (hotspot_y >> 8) & 0xFF

    with open(cur_path, "wb") as f:
        f.write(cur_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert an ICO file into a CUR file with a custom hotspot."
    )
    parser.add_argument("ico_file", help="Input .ico file")
    parser.add_argument("cur_file", help="Output .cur file")
    parser.add_argument("hotspot_x", type=int, help="Hotspot X coordinate")
    parser.add_argument("hotspot_y", type=int, help="Hotspot Y coordinate")

    args = parser.parse_args()

    ico_to_cur(args.ico_file, args.cur_file, args.hotspot_x, args.hotspot_y)
    pause
