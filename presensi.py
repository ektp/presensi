from git import Repo
import config
import datetime

repo = Repo(config.repo)
repo.git.pull('origin', 'master')

repo.git.status()
print(_)

#open file
f=open("README.MD",'a+')
f.read()
f.write('## Log Presensi\nTanggal | Jam | Keterangan\n--- | --- | ---\n')
tanggal = datetime.datetime.now().strftime("%x")
jam = datetime.datetime.now().strftime("%X")
f.write(tanggal)
f.write(' | ')
f.write(jam)
f.write(' | ')
f.write('ket')
f.write('\n')

f.write('# tanggal\nTanggal | Jam | Keterangan\n--- | --- | ---\n')
f.write('# tanggal\nTanggal | Masuk | Pulang\n--- | --- | ---\n')
f.write('# tanggal\nTanggal | Masuk | Pulang\n--- | --- | ---\n')


f.write('1 | 2 | 3\n')
f.close()

repo.git.add("README.MD")
repo.git.commit("pesan")
repo.git.push("origin","master")

