from pathlib import Path
from loggenerator import *

Directory= {
"TextFiles" : [".doc", ".docx", ".log", ".msg", ".odt", ".pages", ".rtf", ".tex", ".txt", ".wpd", ".wps"],
"DataFiles" : [".csv", ".dat", ".ged", ".key", ".keychain", ".pps", ".ppt", ".pptx", ".sdf", ".tar", ".tax2016",
             ".tax2018", ".vcf", ".xml", ".xlr", ".xls", ".xlsx"],
"AudioFiles" : [".aif", ".iff", ".m3u", ".m4a", ".mid", ".mp3", ".mpa", ".wav", ".wma"],
"ImageFiles" : [".bmp", ".dds", ".gif", ".heic", ".jpg", ".png", ".psd", ".psimage", ".tga", ".thm", ".tif", ".tiff",
              ".yuv", ".jpeg"],
"VideoFiles" : [".3g2", ".3gp", ".asf", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".mpg", ".rm", ".srt", ".swf", ".vob",
              ".wmv", ],
"ExecutableFiles" : [".apk", ".app", ".bat", ".cgi", ".com", ".exe", ".gadget", ".jar", ".wsf"],
"WebFiles" : [".asp", ".aspx", ".cer", ".cfm", ".csr", ".css", ".dcr", ".htm", ".html", ".js", ".jsp", ".php", ".rss",
            ".xhtml"],
"CompressedFiles" : [".7z", ".cbr", ".deb", ".gz", ".pkg", ".rar", ".rpm", ".sitx", ".tar", ".zip", ".zipx"],
"DeveloperFiles" : [".c", ".class", ".cpp", ".cs", ".dta", ".fla", ".h", ".java", ".lua", ".m", ".pl", ".py", ".sh",
                  ".sln", ".swift", ".vb", ".vcxproj", ".xcodeproj"]
}

FILE_FORMATS = {file_format: directory
                for directory, file_formats in Directory.items()
                for file_format in file_formats}
currentDir = ("C:\\Users\\hwala\Downloads\\testing")
def filesort(currentDir):
    os.chdir(currentDir)
    try:
        os.mkdir(currentDir + "\Log", 0o755)
    except:
        pass

    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
            addtoLog(currentDir,str(currentDir) +"\\" + str(file_path) + " moved to " + str(currentDir) + "\\" + str(directory_path.joinpath(file_path)))

        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass

    f = open("Log\log.txt", "a")
    f.write("\n####### OPERATION COMPLETE #######\n")
    f.write("\n")
    f.close()



