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

아래 명령으로 배포 → `gh-pages` 브랜치 생성됨.

```bash
uv run mkdocs gh-deploy
```

`github pages` 메뉴에서 `gh-pages`를 사용할 브랜치, `(root)`를 루트 디렉토리로 설정하여 `Save`.
