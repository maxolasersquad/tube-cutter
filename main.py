#! /usr/bin/env python3
import csv
from typing import List, Tuple, Dict
from dataclasses import dataclass, field

@dataclass
class Tube:
    diameter: float
    total_length: float
    segment_lengths: List[float] = field(default_factory=list)

def read_input(file_path: str) -> List[Tube]:
    tubes = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            # Skip empty lines and invalid rows
            if not row or len(row) != 3:
                print(f"Skipping invalid row: {row}")
                continue

            try:
                diameter = float(row[0])
                total_length = float(row[1])
                segment_lengths = list(map(float, row[2].split(',')))
                tubes.append(Tube(diameter, total_length, segment_lengths))
            except ValueError as e:
                print(f"Skipping row with invalid data: {row}. Error: {e}")
                continue
    return tubes

def optimize_cuts(tube: Tube) -> Tuple[int, Dict[int, List[float]], List[float]]:
    segments = sorted(tube.segment_lengths, reverse=True)
    tube_count = 0
    cuts_per_tube: Dict[int, List[float]] = {}
    remaining_segments = segments[:]
    waste_per_tube = []

    while remaining_segments:
        tube_count += 1
        cuts_per_tube[tube_count] = []
        remaining_length = tube.total_length

        for segment in remaining_segments[:]:
            if segment <= remaining_length:
                cuts_per_tube[tube_count].append(segment)
                remaining_length -= segment
                remaining_segments.remove(segment)

        waste_per_tube.append(remaining_length)

    return tube_count, cuts_per_tube, waste_per_tube

def main(input_file: str):
    tubes = read_input(input_file)
    total_waste_all_tubes = 0

    for tube in tubes:
        tube_count, cuts_per_tube, waste_per_tube = optimize_cuts(tube)
        total_waste = sum(waste_per_tube)
        total_waste_all_tubes += total_waste

        print(f"Tube Diameter: {tube.diameter} inches")
        print(f"Total Length: {tube.total_length} inches")
        print(f"Segment Lengths: {tube.segment_lengths}")
        print(f"Number of Tubes Needed: {tube_count}")
        for tube_num, cuts in cuts_per_tube.items():
            print(f"Tube {tube_num} Cuts: {cuts} | Waste: {waste_per_tube[tube_num-1]:.2f} inches")
        print(f"Total Waste for this Tube: {total_waste:.2f} inches\n")

    print(f"Total Waste for All Cuts: {total_waste_all_tubes:.2f} inches")

if __name__ == "__main__":
    input_file = "tube_cuts.psv"
    main(input_file)
    input("Press Enter to exit...")
