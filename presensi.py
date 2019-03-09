from git import Repo
import config
import datetime


def push(id,keterangan,pesan):
	repo = Repo(config.repodir)
	repo.git.pull(config.reponame, config.repobranch)
	repo.git.status()
	#print(_)
	#open file
	f=open(config.repodir+config.mdfile,'a+')
	f.read()
	#f.write('## Log Presensi\nTanggal | Jam | ID | Keterangan\n--- | --- | ---\n')
	tanggal = datetime.datetime.now().strftime("%x")
	jam = datetime.datetime.now().strftime("%X")
	f.write(tanggal)
	f.write(' | ')
	f.write(jam)
	f.write(' | ')
	f.write(id)
	f.write(' | ')
	f.write(keterangan)
	f.write('\n')
	f.close()
	repo.git.add(config.mdfile)
	repo.index.commit(pesan)
	repo.git.push(config.reponame, config.repobranch)

