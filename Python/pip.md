Uninstall only the dependencies and not manually installed packages:
```bash
comm -23 <(pip freeze | sort) <(pip list --not-required --format=freeze | sort) | xargs pip uninstall -y
```

Show only manually installed packages:
```bash
pip list --not-required --format=freeze
```

Delete manually installed packages:
```bash
pip list --not-required --format=freeze | xargs pip uninstall -y
```
