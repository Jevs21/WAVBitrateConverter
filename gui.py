
# import os
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from pydub import AudioSegment
# import logging

# def validate_bitrate(bitrate):
#     if bitrate <= 0:
#         raise ValueError("Bitrate must be a positive integer.")

# def convert_wav_to_lower_bitrate(input_file, output_file, target_bitrate):
#     logging.info(f"Reading input WAV file: {input_file}")
#     audio = AudioSegment.from_wav(input_file)
    
#     logging.info(f"Converting WAV file to a lower bitrate: {target_bitrate} bits per sample")
#     audio = audio.set_frame_rate(int(audio.frame_rate * (target_bitrate / audio.sample_width)))
    
#     logging.info(f"Saving the output WAV file: {output_file}")
#     audio.export(output_file, format="wav")

# def count_wav_files(directory):
#     count = 0
#     for root, _, files in os.walk(directory):
#         for file in files:
#             if file.lower().endswith(".wav"):
#                 count += 1
#     return count

# def convert_directory(input_dir, output_dir, target_bitrate):
#     total_files = count_wav_files(input_dir)
#     completed_files = 0
#     failed_files = []

#     for root, _, files in os.walk(input_dir):
#         for file in files:
#             if file.lower().endswith(".wav") and not file.startswith("."):
#                 input_file = os.path.join(root, file)
#                 relative_path = os.path.relpath(input_file, input_dir)
#                 output_file = os.path.join(output_dir, relative_path)
#                 os.makedirs(os.path.dirname(output_file), exist_ok=True)
                
#                 try:
#                     convert_wav_to_lower_bitrate(input_file, output_file, target_bitrate)
#                 except Exception as e:
#                     failed_files.append(input_file)
#                     logging.error(f"Error converting file: {input_file}, {str(e)}")
                
#                 completed_files += 1
#                 progress_var.set(f"{completed_files}/{total_files}")
#                 app.update_idletasks()

#     return failed_files

# def browse_input_directory():
#     input_directory = filedialog.askdirectory()
#     input_directory_var.set(input_directory)

# def browse_output_directory():
#     output_directory = filedialog.askdirectory()
#     output_directory_var.set(output_directory)

# def convert_button_click():
#     input_directory = input_directory_var.get()
#     output_directory = output_directory_var.get()
#     target_bitrate = target_bitrate_var.get()

#     try:
#         validate_bitrate(target_bitrate)
#         failed_files = convert_directory(input_directory, output_directory, target_bitrate)
#         messagebox.showinfo("Success", "WAV bitrate conversion completed")
#         if failed_files:
#             print("The following files failed to convert:")
#             for file in failed_files:
#                 print(file)
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# app = tk.Tk()
# app.title("WAV Bitrate Converter")

# input_directory_var = tk.StringVar()
# output_directory_var = tk.StringVar()
# target_bitrate_var = tk.IntVar()

# input_frame = tk.Frame(app)
# input_frame.pack(fill=tk.X, padx=10, pady=5)
# tk.Label(input_frame, text="Input directory:").pack(side=tk.LEFT)
# tk.Entry(input_frame, textvariable=input_directory_var).pack(side=tk.LEFT, expand=True, fill=tk.X)
# tk.Button(input_frame, text="Browse", command=browse_input_directory).pack(side=tk.LEFT)

# output_frame = tk.Frame(app)
# output_frame.pack(fill=tk.X, padx=10, pady=5)
# tk.Label(output_frame, text="Output directory:").pack(side=tk.LEFT)
# tk.Entry(output_frame, textvariable=output_directory_var).pack(side=tk.LEFT, expand=True, fill=tk.X)
# tk.Button(output_frame, text="Browse", command=browse_output_directory).pack(side=tk.LEFT)

# bitrate_frame = tk.Frame(app)
# bitrate_frame.pack(fill=tk.X, padx=10, pady=5)
# tk.Label(bitrate_frame, text="Target bitrate:").pack(side=tk.LEFT)
# tk.Spinbox(bitrate_frame, from_=1, to=32, textvariable=target_bitrate_var).pack(side=tk.LEFT)

# progress_label = tk.Label(app, text="Progress: ")
# progress_label.pack(padx=10, pady=5)

# progress_var = tk.StringVar()
# progress_var.set("0/0")
# progress_value_label = tk.Label(app, textvariable=progress_var)
# progress_value_label.pack(padx=10, pady=5)

# convert_button = tk.Button(app, text="Convert", command=convert_button_click)
# convert_button.pack(padx=10, pady=10)

# app.mainloop()







# import os
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from pydub import AudioSegment
# import logging

# def validate_bitrate(bitrate):
#     if bitrate <= 0:
#         raise ValueError("Bitrate must be a positive integer.")

# def convert_wav_to_lower_bitrate(input_file, output_file, target_bitrate):
#     logging.info(f"Reading input WAV file: {input_file}")
#     audio = AudioSegment.from_wav(input_file)
    
#     if audio.sample_width <= target_bitrate:
#         logging.info(f"The input WAV file already has a bitrate of {audio.sample_width} bits per sample, which is equal to or lower than the target bitrate.")
#         return False
    
#     logging.info(f"Converting WAV file to a lower bitrate: {target_bitrate} bits per sample")
#     audio = audio.set_frame_rate(int(audio.frame_rate * (target_bitrate / audio.sample_width)))
    
#     logging.info(f"Saving the output WAV file: {output_file}")
#     audio.export(output_file, format="wav")
#     return True

# def count_wav_files(directory):
#     count = 0
#     for root, _, files in os.walk(directory):
#         for file in files:
#             if file.lower().endswith(".wav"):
#                 count += 1
#     return count

# def convert_directory(input_dir, output_dir, target_bitrate):
#     total_files = count_wav_files(input_dir)
#     completed_files = 0
#     failed_files = []

#     for root, _, files in os.walk(input_dir):
#         for file in files:
#             if file.lower().endswith(".wav"):
#                 input_file = os.path.join(root, file)
#                 relative_path = os.path.relpath(input_file, input_dir)
#                 output_file = os.path.join(output_dir, relative_path)
#                 os.makedirs(os.path.dirname(output_file), exist_ok=True)
                
#                 try:
#                     converted = convert_wav_to_lower_bitrate(input_file, output_file, target_bitrate)
#                     if not converted:
#                         failed_files.append(input_file)
#                 except Exception as e:
#                     failed_files.append(input_file)
#                     logging.error(f"Error converting file: {input_file}, {str(e)}")
                
#                 completed_files += 1
#                 progress_var.set(f"{completed_files}/{total_files}")
#                 app.update_idletasks()

#     return failed_files

# def browse_input_directory():
#     input_directory = filedialog.askdirectory()
#     input_directory_var.set(input_directory)

# def browse_output_directory():
#     output_directory = filedialog.askdirectory()
#     output_directory_var.set(output_directory)

# def convert_button_click():
#     input_directory = input_directory_var.get()
#     output_directory = output_directory_var.get()
#     target_bitrate = target_bitrate_var.get()

#     try:
#         validate_bitrate(target_bitrate)
#         failed_files = convert_directory(input_directory, output_directory, target_bitrate)
#         messagebox.showinfo("Success", "WAV bitrate conversion completed")
#         if failed_files:
#             print("The following files were not converted (already at or below target bitrate):")
#             for file in failed_files:
#                 print(file)
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# app = tk.Tk()
# app.title("WAV Bitrate Converter")

# input_directory_var = tk.StringVar()
# output_directory_var = tk.StringVar()
# target_bitrate_var = tk.IntVar()

# input_frame = tk.Frame(app)
# input_frame.pack(fill=tk.X, padx=10, pady=5)
# tk.Label(input_frame, text="Input directory:").pack(side=tk.LEFT)
# tk.Entry(input_frame, textvariable=input_directory_var).pack(side=tk.LEFT, expand=True, fill=tk.X)
# tk.Button(input_frame, text="Browse", command=browse_input_directory).pack(side=tk.LEFT)

# output_frame = tk.Frame(app)
# output_frame.pack(fill=tk.X, padx=10



import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment
import logging

def validate_bitrate(bitrate):
    if bitrate <= 0:
        raise ValueError("Bitrate must be a positive integer.")

# def convert_wav_to_lower_bitrate(input_file, output_file, target_bitrate):
#     logging.info(f"Reading input WAV file: {input_file}")
#     audio = AudioSegment.from_wav(input_file)
    
#     if audio.sample_width <= target_bitrate:
#         logging.info(f"The input WAV file already has a bitrate of {audio.sample_width} bits per sample, which is equal to or lower than the target bitrate.")
#         shutil.copy(input_file, output_file)
#         return False
    
#     logging.info(f"Converting WAV file to a lower bitrate: {target_bitrate} bits per sample")
#     audio = audio.set_frame_rate(int(audio.frame_rate * (target_bitrate / audio.sample_width)))
    
#     logging.info(f"Saving the output WAV file: {output_file}")
#     audio.export(output_file, format="wav")
#     return True

def convert_wav_to_lower_bitrate(input_file, output_file, target_bitrate):
    try:
        logging.info(f"Reading input WAV file: {input_file}")
        audio = AudioSegment.from_wav(input_file)

        if audio.sample_width * 8 <= target_bitrate:
            logging.info(f"The input WAV file already has a bitrate of {audio.sample_width * 8} bits per sample, which is equal to or lower than the target bitrate.")
            shutil.copy(input_file, output_file)
            return False

        logging.info(f"Converting WAV file to a lower bitrate: {target_bitrate} bits per sample")
        target_sample_width = target_bitrate // 8
        audio = audio.set_sample_width(target_sample_width)

        logging.info(f"Saving the output WAV file: {output_file}")
        audio.export(output_file, format="wav")
        return True

    except Exception as e:
        logging.error(f"An error occurred while processing the file {input_file}: {str(e)}")
        return False

# def convert_wav_to_fixed_bitrate(input_file, output_file):
#     FIXED_BITRATE = 1411  # kbps
#     BITS_PER_BYTE = 8
#     KILO = 1000

#     logging.info(f"Reading input WAV file: {input_file}")
#     audio = AudioSegment.from_wav(input_file)
    
#     target_bits_per_sample = (FIXED_BITRATE * KILO) // (audio.frame_rate * audio.channels) // BITS_PER_BYTE

#     if audio.sample_width * BITS_PER_BYTE <= target_bits_per_sample:
#         logging.info(f"The input WAV file already has a bitrate of {audio.sample_width * BITS_PER_BYTE} bits per sample, which is equal to or lower than the target bitrate.")
#         shutil.copy(input_file, output_file)
#         return False
    
#     logging.info(f"Converting WAV file to a fixed bitrate: {FIXED_BITRATE} kbps")
#     audio = audio.set_frame_rate(int(audio.frame_rate * (target_bits_per_sample / (audio.sample_width * BITS_PER_BYTE))))
    
#     logging.info(f"Saving the output WAV file: {output_file}")
#     audio.export(output_file, format="wav")
#     return True

def count_wav_files(directory):
    count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".wav") and not file.startswith("."):
                count += 1
    return count

# def convert_wav_to_fixed_bitrate(input_file, output_file):
#     FIXED_BITRATE = 1411  # kbps
#     BITS_PER_BYTE = 8
#     KILO = 1000

#     logging.info(f"Reading input WAV file: {input_file}")
#     audio = AudioSegment.from_wav(input_file)

#     target_sample_width_bytes = (FIXED_BITRATE * KILO) // (audio.frame_rate * audio.channels) // BITS_PER_BYTE

#     if audio.sample_width == target_sample_width_bytes:
#         logging.info(f"The input WAV file already has a sample width of {audio.sample_width} bytes per sample, which corresponds to the target bitrate of {FIXED_BITRATE} kbps.")
#         shutil.copy(input_file, output_file)
#         return False

#     logging.info(f"Converting WAV file to a fixed bitrate: {FIXED_BITRATE} kbps")
#     audio = audio.set_sample_width(target_sample_width_bytes)

#     logging.info(f"Saving the output WAV file: {output_file}")
#     audio.export(output_file, format="wav", bitrate=FIXED_BITRATE)
#     return True

def convert_directory(input_dir, output_dir, target_bitrate):
    total_files = count_wav_files(input_dir)
    completed_files = 0

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(".wav") and not file.startswith("."):
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(input_file, input_dir)
                output_file = os.path.join(output_dir, relative_path)
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                
                try:
                    convert_wav_to_lower_bitrate(input_file, output_file, target_bitrate)
                except Exception as e:
                    logging.error(f"Error converting file: {input_file}, {str(e)}")
                
                completed_files += 1
                progress_var.set(f"{completed_files}/{total_files}")
                app.update_idletasks()



def browse_input_directory():
    input_directory = filedialog.askdirectory(initialdir="C:/Users/Jordan/Documents/Music/SP404SAMPLES/!Breaks/RamzoidKit2")
    input_directory_var.set(input_directory)

def browse_output_directory():
    output_directory = filedialog.askdirectory(initialdir="C:/Users/Jordan/Documents/Music/ram")
    output_directory_var.set(output_directory)

def convert_button_click():
    input_directory = input_directory_var.get()
    output_directory = output_directory_var.get()
    target_bitrate = target_bitrate_var.get()

    try:
        validate_bitrate(target_bitrate)
        convert_directory(input_directory, output_directory, target_bitrate)
        messagebox.showinfo("Success", "WAV bitrate conversion completed")
    except Exception as e:
        messagebox.showerror("Error", str(e))




app = tk.Tk()
app.title("WAV Bitrate Converter")

input_directory_var = tk.StringVar()
output_directory_var = tk.StringVar()
target_bitrate_var = tk.IntVar()

input_frame = tk.Frame(app)
input_frame.pack(fill=tk.X, padx=10, pady=5)
tk.Label(input_frame, text="Input directory:").pack(side=tk.LEFT)
tk.Entry(input_frame, textvariable=input_directory_var).pack(side=tk.LEFT, expand=True, fill=tk.X)
tk.Button(input_frame, text="Browse", command=browse_input_directory).pack(side=tk.LEFT)

output_frame = tk.Frame(app)
output_frame.pack(fill=tk.X, padx=10, pady=5)
tk.Label(output_frame, text="Output directory:").pack(side=tk.LEFT)
tk.Entry(output_frame, textvariable=output_directory_var).pack(side=tk.LEFT, expand=True, fill=tk.X)
tk.Button(output_frame, text="Browse", command=browse_output_directory).pack(side=tk.LEFT)

bitrate_frame = tk.Frame(app)
bitrate_frame.pack(fill=tk.X, padx=10, pady=5)
tk.Label(bitrate_frame, text="Target bitrate:").pack(side=tk.LEFT)
tk.Spinbox(bitrate_frame, from_=1, to=32, textvariable=target_bitrate_var).pack(side=tk.LEFT)

progress_label = tk.Label(app, text="Progress: ")
progress_label.pack(padx=10, pady=5)

progress_var = tk.StringVar()
progress_var.set("0/0")
progress_value_label = tk.Label(app, textvariable=progress_var)
progress_value_label.pack(padx=10, pady=5)

convert_button = tk.Button(app, text="Convert", command=convert_button_click)
convert_button.pack(padx=10, pady=10)

app.mainloop()
