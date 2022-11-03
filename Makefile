# sudoで実行
admin:
	@npm i -g vercel

# TODO: 単にdeployするとファイル（requirements.txt）などが更新されない。その場合は、とりあえず、プロジェクトを消して再作成する
deploy:
	@vercel .

run:
	@poetry run python main.py
