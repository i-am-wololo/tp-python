{
	description = "environnement TP";

	inputs = {
		nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
	};

	outputs = {self, nixpkgs, ...}@inputs : {
		devShells.x86_64-linux.default = let 
			pkgs = import nixpkgs {system = "x86_64-linux";};
		in
		pkgs.mkShell {
			packages = with pkgs; [
					(pkgs.python3.withPackages (python-pkgs: [
						python-pkgs.ipython
						python-pkgs.tkinter
    			]))

			];
		};
	};
}
