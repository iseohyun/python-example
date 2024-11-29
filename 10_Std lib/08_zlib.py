### 압축 : zlib, gzip, bz2, lzma, zipfile, tarfile 지원 ###
import zlib

s = b"witch which has which witches wrist watch"
print("원래 데이터 길이: ", len(s), "bytes")

t = zlib.compress(s)
print("zlib압축 후 길이: ", len(t), "bytes")

print("압축 해제: ", zlib.decompress(t))

print("CRC코드: ", zlib.crc32(s))  # 압축 해시, 확인용
