# File Organizer

Automatically organize files into folders based on their extensions, available in both Python and Batch versions.

## Features

- User-friendly interface
- Extension-based organization
- Real-time progress tracking
- Error handling
- Overwrite protection
- Exit option

## Requirements

- For Python: Python 3.6+
- For Batch: Windows OS
- Administrator privileges (for protected folders)

## Files

- `file_organizer.py`: Python version
- `file_organizer.bat`: Batch version

## Usage

### Python Version
```bash
python file_organizer.py
```

### Batch Version
```bash
file_organizer.bat
```

Both versions will:
1. Prompt for source folder path
2. Ask for destination folder name
3. Create organized folders on Desktop
4. Move files automatically

## Example

```
Enter folder path to organize: Downloads
Enter name for destination folder on Desktop: Organized_Files
```

Results in:
```
Desktop/Organized_Files/
    ├── pdf/
    ├── jpg/
    ├── doc/
    └── ...
```

## Error Handling

- Invalid path detection
- Existing folder verification
- Safe exit option

## Contributing

1. Fork repository
2. Create feature branch
3. Submit pull request

## License

MIT License

## Team

**Author:**
- Amir Boutabia

**Support:**
- Salah Eddine Medkour

## Version

1.1.0
