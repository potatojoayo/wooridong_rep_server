from django.db import models


class Address(models.Model):
    # 전체 도로명주소
    roadAddr = models.CharField(max_length=255)
    # 도로명주소 (참고항목 제외)
    roadAddrPart1 = models.CharField(max_length=255, null=True, blank=True)
    # 도로명주소 참고항목
    roadAddrPart2 = models.CharField(max_length=255, null=True, blank=True)
    # 지번주소
    jibunAddr = models.CharField(max_length=255, null=True, blank=True)
    # 영문주소
    engAddr = models.CharField(max_length=255, null=True, blank=True)
    # 우편번호
    zipNo = models.CharField(max_length=5, null=True, blank=True)
    # 행정구역코드
    admCd = models.CharField(max_length=15, null=True, blank=True)
    # 도로명코드
    rnMgtSn = models.CharField(max_length=15, null=True, blank=True)
    # 건물명
    bdNm = models.CharField(max_length=255, blank=True, null=True)
    # 지하여부 (0: 지상, 1: 지하)
    udrtYn = models.CharField(max_length=1, null=True, blank=True)
    # 건물본번
    buldMnnm = models.IntegerField(null=True, blank=True)
    # 건물부번
    buldSlno = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.roadAddr
