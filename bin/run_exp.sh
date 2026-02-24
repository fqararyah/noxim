#!/bin/bash

# --- Configuration Variables (usually stable) ---
NOXIM_BIN="./noxim"
OUTPUT_DIR="outputs"
TRAFFIC_TABLE_DIR="./traffic_tables/"
CONFIG_DIR="../config_examples"
# --- Parameters (usually stable) ---
VERBOSE_LEVEL=2
OTHER_FLAGS="-detailed"


# --- Configuration Variables (change) ---
TRAFFIC_TABLE_FN="tst.txt"
CONFIG_FN="default_configMesh.yaml"
OTUPUT_FN="out_2.txt"

CONFIG_FILE="$CONFIG_DIR/$CONFIG_FN"
TRAFFIC_TABLE_FILE="./$TRAFFIC_TABLE_DIR/$TRAFFIC_TABLE_FN"
OUTPUT_FILE="$OUTPUT_DIR/$OTUPUT_FN"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo "Starting Noxim Simulation..."
echo "Config: $CONFIG_FILE"
echo "Traffic: $TRAFFIC_TABLE"

# --- Execute Command ---
$NOXIM_BIN -config "$CONFIG_FILE" \
           -traffic table "$TRAFFIC_TABLE_FILE" \
           $OTHER_FLAGS \
           -verbose "$VERBOSE_LEVEL" > "$OUTPUT_FILE"

echo "Simulation complete. Results saved to $OUTPUT_FILE"