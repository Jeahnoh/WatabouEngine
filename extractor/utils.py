WINDOW_SIZE = 256
COPY_LENGTH_EXTENT = 4
ESCAPE_BYTE = 0x01

def decompress_tose_lz77(compressed_data):
    buffer = bytearray(WINDOW_SIZE)
    buffer_pos = 0
    output = bytearray()
    i = 0
    
    while i < len(compressed_data):
        byte = compressed_data[i]
        
        if byte != ESCAPE_BYTE:
            # It's a normal pixel. Write it.
            output.append(byte)
            buffer[buffer_pos] = byte
            buffer_pos = (buffer_pos + 1) % WINDOW_SIZE
            i += 1
            
        else: # We hit the Escape Byte
            next_byte = compressed_data[i + 1]
            
            # if we get 0x01 then 0x01 afterwards, then we need to be able to draw 0x01 as a byte for the sprite
            if next_byte == ESCAPE_BYTE:
                # The "Literal Escape" Exception.
                output.append(ESCAPE_BYTE)
                buffer[buffer_pos] = ESCAPE_BYTE
                buffer_pos = (buffer_pos + 1) % WINDOW_SIZE
                i += 2 # Skip over the second ESCAPE_BYTE 
                
            else:
                # A standard LZ77 Copy Command.
                offset = compressed_data[i + 1]
                length_byte = compressed_data[i + 2]
                copy_length = (length_byte & 0x0F) + COPY_LENGTH_EXTENT # ignore first 4 bits in BYTE3 
                
                # Copy from the ring buffer
                for _ in range(copy_length):
                    copied_byte = buffer[offset]
                    output.append(copied_byte)
                    buffer[buffer_pos] = copied_byte
                    buffer_pos = (buffer_pos + 1) % WINDOW_SIZE
                    offset = (offset + 1) % WINDOW_SIZE
                    
                i += 3 # Move past the 3-byte command
                
    return output