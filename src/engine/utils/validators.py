# Validate if a coordinate exits within a list of valid coordinates
def valid_coordinate(coordinate_list, coordinate):
	# Iterate through the list of valid coordinates
	for i in range(0, len(coordinate_list)):
		first = str(coordinate_list[i][0]).replace(" ", "")
		second = str(coordinate_list[i][1]).replace(" ", "")
		coordinate_copy = coordinate.replace(" ", "")
		if coordinate_copy == f'[{first},{second}]':
			return True
	return False
