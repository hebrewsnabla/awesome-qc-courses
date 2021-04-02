db = {
    'no':['m15','m16','m17'],
    'mr':['m18'],
    'lo':['m11'],
}
biz = 'http://mp.weixin.qq.com/s?__biz=MzU5NjMxNjkzMw=='
suf = '&scene=21#wechat_redirect'
art = {
    'm11':['局域分子轨道简介','&mid=2247484784&idx=1&sn=15329ee87c2d8006bb1b87087ea52465&chksm=fe65c31ac9124a0c90ec1ea3576b8d43e17be0f41f4b7fc695c8457a7b19fbb26fd4a80974df'],
'm12':['电子相关计算中的“冻核”近似',''],
'm13':['电子能量的基组外推',''],
'm14': ['用于大体系电子相关计算的Cluster-in-Molecule方法简介',''],
'm15':['S^(1/2)的一些性质','&mid=2247485355&idx=2&sn=6a1a609c84bd5e122c361595f7327e19&chksm=fe65c1c1c91248d7cf39c6aad1986fea5c3f22a57482bea581296ac7149faeeea015760bf0b0'],
'm16': ['从密度矩阵产生自然轨道-理论篇','&mid=2247485355&idx=1&sn=f80b71ea724b4390cc6bc62f220563b3&chksm=fe65c1c1c91248d7ef1fc0ae26ed472bfb1f7a68bbf7d7010303e1a389f6e94f8139193f14d2'],
'm17': ['从密度矩阵产生自然轨道_实战篇（上）','&mid=2247485882&idx=1&sn=d0893bed23e21318fb5a3949d087cdbf&chksm=fe65cfd0c91246c6729439c1623948cad310e2a137a97487ef0b1df5d30e77653e17fa5da23b'],
'm18': ['广义价键波函数（GVB）简介','&mid=2247485870&idx=1&sn=b8a679d449bcaf4f59d5d071a051c392&chksm=fe65cfc4c91246d249c16560c3015dffaccc1b84cf6ee3b3ee31d74a30024708654036c75d5a'],
}

def update():
    for topic, arts in db:
        buf = '## ' + topic + ': \n'
        for a in arts:
            info = art[a]
            buf += '* [' + info[0] + '](' + biz + info[1] + suf + ')\n'
        f.write(buf)



    
       
