import struct 
from utils import pad

def save_pbm(name: str, tab: list[list[int]]):
    handle = open(name, "w");
    handle.write("P1\n");
    handle.write(f"{len(tab)} {len(tab[0])}\n");
    for i in tab:
        for j in i:
            handle.write(str(j)+" ");
        handle.write("\n");
    handle.close();

def carre_blanc(tab_image: list[list[int]]):
    bl_corner = (len(tab_image)-15, 5);
    for i in range(10):
        for j in range(10):
            tab_image[bl_corner[0]+i][bl_corner[1]+j] = 0;

    return tab_image;
def save_pgm(name: str, tab: list[list[int]]):
    handle = open(name, "wb");
    handle.write("P5\n".encode("utf-8"));
    handle.write(f"{len(tab)} {len(tab[0])}\n".encode("utf-8"));
    handle.write("255\n".encode("utf8"));
    for i in tab:
        for j in i:
            handle.write(struct.pack("H", j))
    handle.close()
    return 0

def dessine_rectangle(tab_image: list[list[int]],  x: int, y: int, height: int, length: int, width: int):
    # 4 lines to draw with 
    for i in range(length+1):
        # dessine 2 traits horizontaux
        for j in range(width):
            tab_image[y+j][x+i] = 255
            tab_image[y+height+j][x+i] = 255
        
    for i in range(height+1) :
        # dessine 2 traits verticaux de longueur height et d'épaisseur width
        for j in range(width):
            tab_image[y+i][x+j] = 255
            tab_image[y+i][x+length+j] = 255


# entry point
def main():
    data = [[0 for j in range(500)] for i in range(500)];
    dessine_rectangle(data, 0, 0, 20, 20, 2)
    for i in data:
        print(i)
    save_pgm("empty.pgm", data);

if __name__ == "__main__":
    main()
