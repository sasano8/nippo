# デプロイ

## 初回

初回はvercelにdeployし、`VERCEL_ORG_ID` `VERCEL_PROJECT_ID`などを発行する。
`.vercel`フォルダが作成され、設定が保存される。

```
make deploy
```

- 更新するには再度deployすれがいいが、ファイルが更新されないケースも多々あり、原因がよく分からない
- よく分からない場合は、とりあえずvercelのプロジェクトを削除して実行してみる

## github actions

github actionsでデプロイする場合は、次のシークレットをリポジトリに設定する。
`VERCEL_TOKEN`は自分のvercelアカウントからトークンを発行する。

- VERCEL_ORG_ID
- VERCEL_PROJECT_ID
- VERCEL_TOKEN
