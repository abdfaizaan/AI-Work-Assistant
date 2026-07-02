## Today's Goal

- Understand Python classes using AudioRecorder class in our project.
- Learn Docker fundamentals.
- Revise AzureStorage topics.

## What I learned?

### Python
- Reviewed AudioRecorder class.
- Added comments to understand every function.
- Improved repository documentation.

- Python Concepts
   - Class: A template that defines what an object can do and what data it holds.
   - Object: A real item made from a class, with its own data values.
   - Method: A function inside a class that works on that object's data.
   - self: A keyword used in class methods to refer to the current object.
   - __init__(): A special method that runs when a new object is created and sets it up.

## Azure

   - Storage Account: The top-level Azure storage resource that holds containers and blobs.
   - Container: A logical group inside a storage account used to organize blobs.
   - Blob: A file or data object stored in Azure Storage.
   - Redundancy: Keeping extra copies of data so it is safe if something fails.
   - LRS: Locally Redundant Storage keeps copies in the same region.
   - ZRS: Zone-Redundant Storage keeps copies across different zones inside one region.
   - GRS: Geo Redundant Storage keeps copies in another region for disaster recovery.
   - GZRS: GeoZone Redundant Storage keeps copies in multiple zones and regions.
   - Storage Tiers: Different cost and performance levels for storing data.
   - Hot: Used for data that is accessed frequently.
   - Cool: Used for data accessed less often and costs less than hot storage.
   - Archive: Used for long-term storage of data that is rarely accessed.
   - Authentication: The process of proving identity before accessing storage.
   - SAS: Shared Access Signature is a temporary permission link for storage access.
   - Access Keys: Permanent keys that give full access to a storage account.

## Devops
- Docker: A tool that packages applications into containers so they run the same anywhere.
- Image: A saved version of an app and everything it needs to run.
- Container: A running instance of an image.
- VM vs Container: A VM runs a full virtual machine with its own operating system, while a container shares the host OS and is much lighter.

## Git
- git log --oneline: Shows a simple history of recent commits, one line per commit.
- git status: Shows what files have changed and what is ready to be committed.
- git add: Marks changed files so they will be included in the next commit.
- git commit: Saves the staged changes in the local repository as a new version.
- git push: Sends your local commits to the remote repository so others can see them.

