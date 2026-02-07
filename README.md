# 패키지 빌드 및 Docs 제작

## 환경 설정
```bash
uv sync --all-groups
```

## 패키지 빌드
```bash
uv build
```

## mkdocs 문서 호스팅
```bash
uv run mkdocs serve
```

## mkdocs 문서 빌드
```bash
uv run mkdocs build
```

## mkdocs 문서 github pages로 배포
```bash
uv run mkdocs gh-deploy
```