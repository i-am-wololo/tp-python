import struct 

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
        for j in range(10):;
            tab_image[bl_corner[0]+i][bl_corner[1]+j] = 0;

    return tab_image;

def save_pgm(name: str, tab: list[list[int]]):
    handle = open(name, "wb");
    handle.write("P5\n".encode("utf-8"))
    for i in tab:
        for j in i:
            handle.write()
    handle.write("\n".encode("utf-8"))

def dessine_rectangle(tab_image: list[list[int]],  x: int, y: int, width: int, length: int, thickness: int):
    pass


# entry point
def main():
    data = [[1 for j in range(100)] for i in range(100)];
    data = carre_blanc(data);
    save_pbm("empty.pbm", data);

if __name__ == "__main__":
    main()
