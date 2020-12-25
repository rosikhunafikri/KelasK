import ffmpeg

if __name__ == "__main__":
    input_stream = ffmpeg.input('nomor5/input.mp4', f='mp4')
    output_stream = ffmpeg.output(input_stream, 'nomor5/output/output.m3u8', format='hls', start_number=0, hls_time=5, hls_list_size=0)
    ffmpeg.run(output_stream)