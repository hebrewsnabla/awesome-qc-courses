
section = {
	'no': '自然轨道',
	'mr': '多参考',
	'lo': '局域轨道',
	'mok':'MOKIT依赖程序'
}
db = {
    'no':['m15','m16','m17'],
    'mr':['m18', 'g33','g35','g36','mok1','mok3','z1'],
    'lo':['m11','z8','mok3'],
    'mok':['mok1','gam1','p2','p5','om1','om2']
}
biz = 'http://mp.weixin.qq.com/s?__biz=MzU5NjMxNjkzMw=='
suf = '&scene=21#wechat_redirect'
art = {
# 方法原理
    'm11':['局域分子轨道简介',
        '&mid=2247484784&idx=1&sn=15329ee87c2d8006bb1b87087ea52465&chksm=fe65c31ac9124a0c90ec1ea3576b8d43e17be0f41f4b7fc695c8457a7b19fbb26fd4a80974df'],
    'm12':['电子相关计算中的“冻核”近似',''],
    'm13':['电子能量的基组外推',''],
    'm14': ['用于大体系电子相关计算的Cluster-in-Molecule方法简介',''],
    'm15':['S^(1/2)的一些性质','&mid=2247485355&idx=2&sn=6a1a609c84bd5e122c361595f7327e19&chksm=fe65c1c1c91248d7cf39c6aad1986fea5c3f22a57482bea581296ac7149faeeea015760bf0b0'],
    'm16': ['从密度矩阵产生自然轨道-理论篇',
        '&mid=2247485355&idx=1&sn=f80b71ea724b4390cc6bc62f220563b3&chksm=fe65c1c1c91248d7ef1fc0ae26ed472bfb1f7a68bbf7d7010303e1a389f6e94f8139193f14d2'],
    'm17': ['从密度矩阵产生自然轨道_实战篇（上）',
        '&mid=2247485882&idx=1&sn=d0893bed23e21318fb5a3949d087cdbf&chksm=fe65cfd0c91246c6729439c1623948cad310e2a137a97487ef0b1df5d30e77653e17fa5da23b'],
    'm18': ['广义价键波函数（GVB）简介','&mid=2247485870&idx=1&sn=b8a679d449bcaf4f59d5d071a051c392&chksm=fe65cfc4c91246d249c16560c3015dffaccc1b84cf6ee3b3ee31d74a30024708654036c75d5a'],
# 软件
    'g33': ['用Gaussian做CASSCF计算','&mid=2247485729&idx=1&sn=6020c637f5cfbf59ece9e9bf9f5ade98&chksm=fe65cf4bc912465d9191755e923928510b7c218316ea7cfd10df6ce3207ec4df5f18539c4655'],
    'g35':['用Gaussian寻找圆锥交叉点 ','&mid=2247485767&idx=1&sn=541e88da033803bf789a903734263a3e&chksm=fe65cf2dc912463b163216507e7ff476b7c0d07553a8c6115b6ba091b33a0695d75099f14cee'],
    'g36':['广义价键计算及初始轨道的构造', '&mid=2247486021&idx=1&sn=38b81ef6ea2e522f97aebc472ce68a48&chksm=fe65cc2fc9124539ec4ce4ff984ab8c68b287bf7da4459b930bab29e0b90e684112f286d6e3e'],
    'mok1':['自动做多参考态计算的程序MOKIT ',
        '&mid=2247486051&idx=1&sn=88c54f08bb614f293e659b233ddeb26d&chksm=fe65cc09c912451f858c29f8ee28707f2df713c17450984dcf6280513272ba7761c5ce9650d7'],
    'mok3':['CASSCF初始轨道高效构建（一）：局域轨道 ',
        '&mid=2247486290&idx=1&sn=f2ff27ee8bbe299ee68be03c303171c3&chksm=fe65cd38c912442eebc9f7e41c0f6e228f9ebed2f2bd5493a2eda3f1a4a1c07a4d25707a9989'],
    'gam1':['GAMESS编译教程 ','&mid=2247483886&idx=1&sn=c06c747a0c473e0f1928b6f10f139051&chksm=fe65c784c9124e92d52b88b122acbec5439fe155ad6cbe2b7a902223387502dbbdae663e19aa'],
    'p2':['离线安装PySCF程序（1.5及更高版本） ', 
        '&mid=2247485142&idx=1&sn=8eb5f851f70f20a9701e646e84c82678&chksm=fe65c0bcc91249aac92d6eead2aee25fd49f9eecb12d78b866cf025714d36409073c34ac4d8d'],
    'p5':['Block-1.5的编译和安装 ',
        '&mid=2247484244&idx=1&sn=2fadac7d7b39ef1befac3e9952b709ab&chksm=fe65c53ec9124c28e0ac1b91c72868b0e6e19de9adb5315515976a0d3e9185debcab59bbf0ce'],
    'om1':['OpenMolcas 与 QCMaquis 的安装 ',
        '&mid=2247484039&idx=1&sn=2b704a9d598f7d5501f0a5f2ed886b78&chksm=fe65c4edc9124dfbd958ec2db4a228aa8eb3930a8138b2ca07fabc7f37c3ca16473ffc8c704f'],
    'om2':['离线编译OpenMolcas+QCMaquis ',
        '&mid=2247486188&idx=1&sn=291723e34570bef5db189ca9dbd35dce&chksm=fe65cc86c912459013dd162f604ea9bb77eddaddb1cc7e6bdbf81b57e15dbcb0afa69742c077'],
# 综合教程
    'z1':['激发态计算之如何选取特定的分子轨道作为活性空间 ',
        '&mid=2247484238&idx=1&sn=4f244a96c45dabdde29b103c2e8ef165&chksm=fe65c524c9124c32703430b2fca595e4c2928b7528a79ba478c34c30909a261d51979efac8ad'],
    'z8':['利用常见的程序做轨道局域化 ',
        '&mid=2247485018&idx=1&sn=d97820ffde2e86f339dd5c257d5a424d&chksm=fe65c030c9124926db55cd5c999ebca8229b8e167c39226db883a2b869dd520ddd43aad3c648']
}
def update():
    f = open('qc-wx.md', 'w')
    for topic, arts in db.items():
        buf = '## ' + section[topic] + ': \n'
        for a in arts:
            #print(a)
            info = art[a]
            buf += '* [' + info[0] + '](' + biz + info[1] + suf + ')\n'
        f.write(buf)
    f.close()

if __name__ == '__main__':
    update()

    
       
