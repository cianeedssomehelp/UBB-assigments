from src.repository.repoMemory import BookMemoryRepo
from src.repository.repositoryBinary import BinaryFileRepository
from src.repository.repositoryText import BookTextFileRepo
from src.services.services import Services
from src.ui.ui import UI

def main():
    try:
        repository = int(input("Enter which repository you would like to use (1. Memory repo, 2. Binary repo or 3. Text repo): "))
        if repository < 1:
            raise ValueError("Invalid repository")
        elif repository > 3:
            raise ValueError("Invalid repository")
        elif repository == 1:
            repo = BookMemoryRepo()
        elif repository == 2:
            filename = input("Enter filename: ").strip()
            repo = BinaryFileRepository(filename)
        elif repository == 3:
            repo = BookTextFileRepo()
        else:
            raise ValueError("Invalid repository. Please choose a number between 1 and 3 for your repository.")
        services = Services(repo)
        ui = UI(services)
        ui.start([])
    except Exception as error:
        print(error)
if __name__ == "__main__":
    main()
