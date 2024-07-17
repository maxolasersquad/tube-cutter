# Tube Cutter

This is a simple script to determine the optimum strategy for cutting tubes to
minimize waste.

## Description

The Tube Cutter script reads tube diameters, total tube lengths, and the
required segment lengths from a PSV file. It then calculates the optimal cutting
strategy to minimize waste. The script provides a detailed breakdown of the cuts
made for each tube and the resulting waste. At the end, it also provides the
total waste for all cuts.

## Features

- Reads input data from a PSV file
- Calculates the optimal cutting strategy to minimize waste
- Provides detailed cuts and waste information for each tube
- Summarizes total waste for all cuts

## Requirements

This script uses only Python's standard library, so no external libraries are required.

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python installed (version 3.7 or higher).

## Usage

1. Prepare your input PSV file (`tube_cuts.psv`). The file should have the
   following format:

    ```psv
    3|60|20,18,15
    2.5|50|14,13,12.5
    ```

2. Run the script:

    ```sh
    ./tube_cutter.py
    ```

3. The script will read the input file, process the data, and print the results
   to the console.

## Example

Given an input file `tube_cuts.psv` with the following contents:

```psv
3|60|20,18,15
2.5|50|14,13,12.5
```

Running the script will produce an output similar to this:

```plaintext
Tube Diameter: 3.0 inches
Total Length: 60.0 inches
Segment Lengths: [20.0, 18.0, 15.0]
Number of Tubes Needed: 1
Tube 1 Cuts: [20.0, 18.0, 15.0] | Waste: 7.00 inches
Total Waste for this Tube: 7.00 inches

Tube Diameter: 2.5 inches
Total Length: 50.0 inches
Segment Lengths: [14.0, 13.0, 12.5]
Number of Tubes Needed: 1
Tube 1 Cuts: [14.0, 13.0, 12.5] | Waste: 10.50 inches
Total Waste for this Tube: 10.50 inches

Total Waste for All Cuts: 17.50 inches
```

## License

This project is licensed under the GNU General Public License v3.0. See the
[LICENSE file](LICENSE) for details.
