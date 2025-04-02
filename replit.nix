{pkgs}: {
  deps = [
    pkgs.kodiPackages.requests
    pkgs.python39Packages.requests
    pkgs.python38Packages.beautifulsoup4
    pkgs.python39Packages.fastapi
    pkgs.python38Packages.fastapi
    pkgs.python39Packages.uvicorn
  ];
}
