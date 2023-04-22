import argparse
import sys
import logging
from pydub import AudioSegment

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert WAV file to a lower bitrate.")
    parser.add_argument("input_file", help="Path to the input WAV file.")
    parser.add_argument("output_file", help="Path to the output WAV file.")
    parser.add_argument("target_bitrate", type=int, help="Target bitrate (in bits per sample).")
    parser.add_argument("--log", action="store_true", help="Enable logging.")
    return parser.parse_args()

def setup_logging(enable_logging):
    log_level = logging.DEBUG if enable_logging else logging.WARNING
    logging.basicConfig(level=log_level, format="%(asctime)s [%(levelname)s] %(message)s")

def validate_bitrate(bitrate):
    if bitrate <= 0:
        raise ValueError("Bitrate must be a positive integer.")

def convert_wav_to_lower_bitrate(input_file, output_file, target_bitrate):
    logging.info(f"Reading input WAV file: {input_file}")
    audio = AudioSegment.from_wav(input_file)
    
    logging.info(f"Converting WAV file to a lower bitrate: {target_bitrate} bits per sample")
    audio = audio.set_frame_rate(int(audio.frame_rate * (target_bitrate / audio.sample_width)))
    
    logging.info(f"Saving the output WAV file: {output_file}")
    audio.export(output_file, format="wav")

def main():
    args = parse_arguments()
    setup_logging(args.log)
    
    logging.info("Starting the WAV bitrate conversion process")
    validate_bitrate(args.target_bitrate)
    convert_wav_to_lower_bitrate(args.input_file, args.output_file, args.target_bitrate)
    logging.info("WAV bitrate conversion completed")

if __name__ == "__main__":
    main()
