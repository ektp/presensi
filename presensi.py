from git import Repo
import config
import datetime

repo = Repo(config.repo)
repo.git.pull('origin', 'master')

repo.git.status()
print(_)

#open file
f=open(config.repo+"README.md",'a+')
f.read()
#f.write('## Log Presensi\nTanggal | Jam | Keterangan\n--- | --- | ---\n')
tanggal = datetime.datetime.now().strftime("%x")
jam = datetime.datetime.now().strftime("%X")
f.write(tanggal)
f.write(' | ')
f.write(jam)
f.write(' | ')
f.write('ID')
f.write(' | ')
f.write('ket')
f.write('\n')
f.close()

repo.git.add("README.md")
repo.git.commit("pesan")
repo.git.push("origin","master")

