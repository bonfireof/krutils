'''
    COMMON UTIL
        WARN : 다른 프로젝트 파일과 연관이 없도록 독립적으로 구성
'''

import os
from datetime import datetime as dt


##########################################
# 문자 관리
##########################################


def is_empty(input: str) -> bool():
    '''
    String 문자열이 빈문자열 또는 None 인 경우에 True를 반환한다
    이외의 인스턴스가 입력되면 오류를 반환.
    '''

    # print("[" + str(input) + "]" + str(type(input)))

    if input == None:
        return True

    elif (isinstance(input, str) == True):

        input = input.strip()
        # print("[" + input + "] is trimed.")

        if len(input) == 0:
            return True
        else:
            return False

    else:
        raise Exception("NaN")



#     /** <b> 문자열비교 </b> */
#     public static int strcmp(String str1, String str2)
#     {
#         return StringUtils.strcmp(str1, str2);
#     }


#     /** 한글여부 */
#     public static boolean isHangul(char inputChar)
#     {
#         return StringUtils.isHangul(inputChar);
#     }


#     /** 한글여부 */
#     public static boolean isHangul(String inString, boolean full)
#     {
#         return StringUtils.isHangul(inString, full);
#     }


#     /** 한글 포함여부 */
#     public static boolean hasHangul(String inString)
#     {
#         return StringUtils.isHangul(inString, false);
#     }


#     /** 숫자여부 */
#     public static boolean isDigit(String inString)
#     {
#         return StringUtils.isDigit(inString);
#     }


#     /** <b> null 대체 </b> */
#     public static Object nvl(Object obj, Object rvalue)
#     {
#         return StringUtils.nvl(obj, rvalue);
#     }


#     /** <b> null 대체 </b> */
#     public static String nvl(String str, String rStr)
#     {
#         return StringUtils.nvl(str, rStr);
#     }


#     /** <b> null 대체 </b> */
#     public static String nvl(String str)
#     {
#         return StringUtils.nvl(str);
#     }


#     /** <b> 문자열 대체 </b> */
#     public static String replace(String inString, String oldSubstring, String newSubstring)
#     {
#         return StringUtils.replace(inString, oldSubstring, newSubstring);
#     }


#     /** <b> 문자열 자르기 </b> */
#     public static String[] split(String toSplit, String delimiter)
#     {
#         return StringUtils.split(toSplit, delimiter);
#     }


#     /** <b> 문자열(한글) 자르기 </b> */
#     public static String substringKorean(String inString, int length, String encoding) // by Shin Changyoung 2013.03.06
#     {
#         return StringUtils.substringKorean(inString, length, encoding);
#     }


#     /**
#      * <b> 문자열 자르기 </b>
#      * <p><pre>
#      *  EXCEL 함수 MID()와 동일한 처리
#      *  범위를 넘어가도 오류발생하지 않음
#      * </pre></p>
#      */
#     public static String mid(String str, int strtIdx, int len)
#     {
#         return StringUtils.midh(str, strtIdx, len);
#     }
# //    public static String mid(String str, int strtIdx, int len)
# //    {
# //        return StringUtils.mid
# //    }


#     /**
#      * <b> 문자열(한글) 자르기 </b>
#      * <p><pre>
#      *  EXCEL 함수 MIDB()와 동일한 처리
#      *  범위를 넘어가도 오류발생하지 않음
#      * </pre></p>
#      *
#      * [코딩 예]
#      * <pre><code>
#      *
#      *      "a가나"  = midh("a가나다bcd", 0, 6);
#      *      "가나다" = midh("a가나다bcd", 1, 6);
#      *      "나다b"  = midh("a가나다bcd", 2, 6);
#      *      "나다bc" = midh("a가나다bcd", 3, 6);
#      *      "다bcd"  = midh("a가나다bcd", 4, 6);
#      *      "다bcd"  = midh("a가나다bcd", 5, 6);
#      *      "bcd"    = midh("a가나다bcd", 6, 6);
#      *      "bcd"    = midh("a가나다bcd", 7, 6);
#      *      "cd"     = midh("a가나다bcd", 8, 6);
#      *      "d"      = midh("a가나다bcd", 9, 6);
#      *      ""       = midh("a가나다bcd", 10, 6);
#      *      ""       = midh("a가나다bcd", 11, 6);
#      *
#      * </code></pre>
#      *
#      *
#      **/
#     public static String midh(String str, int strtIdx, int len)
#     {
#         return StringUtils.midh(str, strtIdx, len);
#     }


#     /** 좌측 채우기 */
#     public static String lpad(String str, int length, String pad)
#     {
#         return StringUtils.lpad(str, length, pad);
#     }


#     /** 우측 채우기 */
#     public static String rpad(String str, int length, String pad)
#     {
#         return StringUtils.rpad(str, length, pad);
#     }


#     /**
#      * <b> lpad </b>
#      * <p><pre>
#      *  한글을 2byte로 처리하여 len길이만큼의 pad를 덧붙여 문자열 생성
#      * </pre></p>
#      **/
#     public static String lpadByte(String inputStr, int len, String pad)
#     {
#         return StringUtils.lpadByte(inputStr, len, pad);
#     }


#     /**
#      * <b> rpad </b>
#      * <p><pre>
#      *  한글을 2byte로 처리하여 len길이만큼의 pad를 덧붙여 문자열 생성
#      * </pre></p>
#      **/
#     public static String rpadByte(String inputStr, int len, String pad)
#     {
#         return StringUtils.rpadByte(inputStr, len, pad);
#     }


#     public static int getByte(String inputStr)
#     {
#         return StringUtils.getByte(inputStr);
#     }


#     /**
#      * <b> 문자열 마스킹 처리 </b>
#      * <p><pre>
#      *  orgStr 문자열을 strtPos부터 시작하여 len길이만큼 maskChar로 치환한다
#      *
#             *  ※ strtPos : array index 를 기준함. 0부터 시작
#             *  ※ len  : byte단위라 아닌 character 단위를 사용함. 즉, 한글 1글자는 길이 1로 계산됨.
#      *
#      *  사용예> "가a나****d마e바f사g" = setMaskStr("가a나b다c라d마e바f사g", 3, 4, '*');
#      *
#      * </pre></p>
#      *
#      * @param       orgStr      마스킹 처리할 문자열
#      * @param       strtPos     마스킹 문자의 시작위치(0부터 시작)
#      * @param       len         마스킹 문자의 길이
#      * @param       maskChar    마스킹 문자
#      * @return      maskStr     마스킹 처리된 문자열
#      *
#      */
#     public static String setMaskStr(String orgStr, int strtPos, int len, char maskChar)
#     {
#         return StringUtils.setMaskStr(orgStr, strtPos, len, maskChar);
#     }


#     /**
#      * <b> 마스킹 문자열 만들기 </b>
#      * <p><pre>
#      *  입력된 길이(byte)만큼 연속된 "*"문자열을 만든다
#      *
#      *  사용예>
#      *      "***"            = genMaskStr(3);
#      *      "*****"          = genMaskStr(PAConst.MASK_LEN);
#      *      "*************"  = genMaskStr(PAConst.MASK_LEN_CONT_NO);
#      * </pre></p>
#      *
#      * @param       int length
#      * @return      String maskedString
#      */
#     public static String genMaskStr(int len)
#     {
#         return StringUtils.genMaskStr(len);
#     }


#     /**
#      * Integer.parseInt()와 같지만 문자열이 null, "", 공백문자열일 경우 0을 돌려준다
#      */
#     public static int parseStringAsIntVl( String str )
#     {
#         return StringUtils.parseStringAsIntVl(str);
#     }

#     //////////////////////////////////////////
#     //      argument (프로그램 실행 인자)
#     //////////////////////////////////////////
#     /**
#      * <b> 입력된 인자 목록 </b>
#      * <p><pre>
#      *  argName=argVal 형식의 String[]를 split하여 변수명 추출
#      * </pre></p>
#      */
#     public static List<String> getArgList(String[] orgArgStrArr)
#     {
#         return ArgumentUtils.getArgList(orgArgStrArr);
#     }
#     /**
#      * <b> 입력된 인자 값 추출 </b>
#      * <p><pre>
#      *  argName=argVal 형식의 String[]를 split하여 값 추출
#      * </pre></p>
#      */
#     public static String getArgValue(String[] orgArgStrArr, String argName)
#     {
#         return ArgumentUtils.getArgValue(orgArgStrArr, argName);
#     }
#     /**
#      * <b> 입력된 인자 값 추출. 값이 존재하지 않는 경우 기본값으로 대체 </b>
#      * <p><pre>
#      *  argName=argVal 형식의 String[]를 split하여 값 추출
#      * </pre></p>
#      */
#     public static String getArgValue(String[] orgArgStrArr, String argName, String nvlValue)
#     {
#         return ArgumentUtils.getArgValueNvl(orgArgStrArr, argName, nvlValue);
#     }




##########################################
##      날짜 관리
##########################################


def curr_timestamp() -> str:
    '''현재일시'''
    return dt.now().strftime("%Y%m%d%H%M%S%f")


def curr_date() -> str:
    '''현재일자'''
    return dt.now().strftime("%Y%m%d")


def curr_time() -> str:
    '''현재시각'''
    return dt.now().strftime("%H%M%S")


def curr_quarter() -> int:
    '''현재분기'''
    curr_month = int(dt.now().strftime("%m"))
    curr_quarter = int((curr_month + 2) / 3)
    return curr_quarter


# 몇분기 인가?
# 분기중 몇째주인가? (인자 : 시작요일)
# 월중 몇째주인가? (인자 : 시작요일)
# yyyymm의 첫 xx 요일의 날짜는 언제인가?
# yyyymmdd 까지 남은 날짜는 몇일인가?
# yyyymmdd 까지 남은 날짜는 몇분인가?


#     //////////////////////////////////////////
#     //      금액(BigDecimal) 관련 연산
#     //////////////////////////////////////////
#     /**
#      * <b> ADD 연산 </b>
#      *
#      * <p>
#      * 소수점 반올림 15자리
#      * </p>
#      *
#      * @see     BigDecimal#add()
#      */
#     public static BigDecimal add(BigDecimal original, BigDecimal augend)
#     {
#         return NumberUtils.add(original, augend);
#     }


#     /**
#      * <b> SUBSTRACT 연산 </b>
#      *
#      * <p>
#      * 소수점 반올림 15자리
#      * </p>
#      *
#      * @see     BigDecimal#substract()
#      */
#     public static BigDecimal subtract(BigDecimal original, BigDecimal subtrahend)
#     {
#         return NumberUtils.subtract(original, subtrahend);
#     }


#     /**
#      * <b> MULTIPLY 연산 </b>
#      *
#      * <p>
#      *  곱셈연산. 입력받은 소수점 자리 미만 버림
#      * </p>
#      *
#      * @see     BigDecimal#multiply()
#      */
#     public static BigDecimal multiplyPrec(BigDecimal original, BigDecimal multiplicand, int precision)
#     {
#         return NumberUtils.multiplyPrec(original, multiplicand, precision);
#     }


#     /**
#      * <b> MULTIPLY 연산 </b>
#      *
#      * <p>
#      *  곱셈연산. 소수점 15자리 미만 버림
#      * </p>
#      *
#      * @see     BigDecimal#multiply()
#      */
#     public static BigDecimal multiplyPrec(BigDecimal original, BigDecimal multiplicand)
#     {
#         return NumberUtils.multiplyPrec(original, multiplicand);
#     }


#     /**
#      * <b> MULTIPLY 연산 </b>
#      *
#      * <p>
#      *  곱셈연산. 입력받은 소수점 자리로 반올림하여 리턴
#      * </p>
#      *
#      * @see     BigDecimal#multiply()
#      */
#     public static BigDecimal multiplyR(BigDecimal original, BigDecimal multiplicand, int precision)
#     {
#         return NumberUtils.multiplyR(original, multiplicand, precision);
#     }


#     /**
#      * <b> MULTIPLY 연산 </b>
#      *
#      * <p>
#      *  곱셈연산. 소수점 15자리로 반올림하여 리턴
#      * </p>
#      *
#      * @see     BigDecimal#multiply()
#      */
#     public static BigDecimal multiplyR(BigDecimal original, BigDecimal multiplicand)
#     {
#         return NumberUtils.multiplyR(original, multiplicand);
#     }


#     /**
#      * <b> DIV 연산 </b>
#      * <p><pre>
#      * 소수점 15자리로 반올림된 BigDecimal을 return
#      * </pre></p>
#      *
#      * [코딩 예]
#      * <pre><code>
#      *      Bigdecimal retVl = divR(BigDecimal.valueOf(14.1), BigDecimal.valueOf(4));
#      * </code></pre>
#      *
#      * @see         BigDecimal#divide()
#      *
#      */
#     public static BigDecimal divR(BigDecimal original, BigDecimal divisor)
#     {
#         return NumberUtils.divR(original, divisor);
#     }


#     /**
#      * <b> DIV 연산 </b>
#      * <p><pre>
#      * 입력받은 소수점 자리로 반올림된 BigDecimal을 return
#      * </pre></p>
#      *
#      * [코딩 예]
#      * <pre><code>
#      *      Bigdecimal retVl = divR(BigDecimal.valueOf(14.1), BigDecimal.valueOf(4), 0);
#      * </code></pre>
#      *
#      */
#     public static BigDecimal divR(BigDecimal original, BigDecimal divisor, int precision)
#     {
#         return NumberUtils.divR(original, divisor, precision);
#     }


#     /**
#      * <b> DIV 연산 </b>
#      * <p><pre>
#      * 소수점 15자리로 절사된 BigDecimal을 return
#      * </pre></p>
#      *
#      * [코딩 예]
#      * <pre><code>
#      *      Bigdecimal retVl = divR(BigDecimal.valueOf(14.1), BigDecimal.valueOf(4));
#      * </code></pre>
#      *
#      */
#     public static BigDecimal div(BigDecimal original, BigDecimal divisor)
#     {
#         return NumberUtils.div(original, divisor);
#     }


#     /**
#      * <b> DIV 연산 </b>
#      * <p><pre>
#      * 입력받은 소수점 자리로 절사된 BigDecimal을 return
#      * </pre></p>
#      *
#      * [코딩 예]
#      * <pre><code>
#      *      Bigdecimal retVl = divR(BigDecimal.valueOf(14.1), BigDecimal.valueOf(4), 0);
#      * </code></pre>
#      *
#      */
#     public static BigDecimal div(BigDecimal original, BigDecimal divisor, int precision)
#     {
#         return NumberUtils.div(original, divisor, precision);
#     }


#     /**
#      * <b> POWER 연산 </b>
#      *
#      * <p>
#      * 소수점 반올림 15자리
#      * </p>
#      *
#      * @see     BigDecimal#pow()
#      */
#     public static BigDecimal pow(BigDecimal a, double b)
#     {
#         return pow(a.doubleValue(), b);
#     }
#     private static BigDecimal pow(double a, double b)
#     {
#         return NumberUtils.pow(a, b);
#     }




##########################################
##      FILE, DIRECTORIES
##########################################

def find_first_file_to_root(file_name: str) -> str:
    '''
    file_name을 최상위 디렉토리까지 올라가며 찾는다.
    첫번째 확인된 경로를 리턴한다.
    '''
    if is_empty(file_name):
        raise Exception('찾고자하는 파일명을 입력해 주세요')

    import os

    curr_dir = os.path.dirname(__file__)
    # print("curr_dir[{0}]".format(curr_dir))

    file_path = ""
    for ii in range(100):
        # print("[{0}] {1}".format(ii, curr_dir))

        if (os.path.isfile(curr_dir + "/" + file_name) == True):
            file_path = os.path.join(curr_dir, file_name)
            # print("찾았다!", file_path)
            break
        else:
            # print("상위로 찾아 올라간다[{0}]->[{1}]".format(curr_dir, os.path.abspath(os.path.join(curr_dir, '..'))))
            # root까지 확인된 경우 : 더이상 찾을 수 없을 때
            if (curr_dir == os.path.abspath(os.path.join(curr_dir, '..'))):
                # print("못찾았다!")
                #raise Exception(file_name + " 파일을 찾을 수 없습니다.")
                return None
            else:
                curr_dir = os.path.abspath(os.path.join(curr_dir, '..'))

    # print("find_first_file_to_root() -> [{0}]".format(file_path))
    return file_path






















##########################################
##      JSON
##########################################



def get_json_as_dic(file_path=None) -> dict():
    '''
       "xxx.json"  file을 읽어 dict형태로 반환한다.

       ex> get_json_file("./config/setting.json")
    '''

    # do something
    pass


def is_connectable_internet() -> bool():

    if (checkInternetHttplib() == True or
            checkInternetSocket() == True):
        return True

    else:
        return False


def checkInternetHttplib(url="www.google.com", timeout=3):

    import http.client as httplib

    conn = httplib.HTTPConnection(url, timeout=timeout)

    try:
        conn.request("HEAD", "/")
        conn.close()
        return True

    except Exception as e:
        # print(e)
        return False


def checkInternetSocket(host="8.8.8.8", port=53, timeout=3):

    import socket

    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True

    except socket.error as ex:
        # print(ex)
        return False


def get_katis_env() -> dict():

    # 실행환경 설정 파일 읽기
    katis_file_path = get_katis_config_file_path()

    if (len(katis_file_path) == 0):
        return False

    import json
    with open(katis_file_path) as kf:
        katis_env = json.load(kf)

    # print(type(katis_env))
    return katis_env


def get_katis_config_file_path() -> str:

    import os

    curr_dir = os.path.dirname(__file__)
    # print("curr_dir[{0}]".format(curr_dir))

    katis_config_file_path = ""
    # while True:
    for ii in range(5):
        # print("[{0}] {1}".format(ii, curr_dir))

        if (os.path.isfile(curr_dir + "/" + CONST.KATIS_CONFIG_FILE_NAME) == True):
            katis_config_file_path = os.path.join(curr_dir, CONST.KATIS_CONFIG_FILE_NAME)
            # print("찾았다!", katis_config_file_path)
            break
        else:
            # print("상위로 찾아 올라간다[{0}]->[{1}]".format(curr_dir, os.path.abspath(os.path.join(curr_dir, '..'))))
            # root까지 확인된 경우 : 더이상 찾을 수 없을 때
            if (curr_dir == os.path.abspath(os.path.join(curr_dir, '..'))):
                # print("못찾았다!")
                raise Exception(CONST.KATIS_CONFIG_FILE_NAME + " 파일을 찾을 수 없습니다.")
                break
            else:
                curr_dir = os.path.abspath(os.path.join(curr_dir, '..'))

    # print("get_katis_config_file_path() -> [{0}]".format(katis_config_file_path))
    return katis_config_file_path

















#     //////////////////////////////////////////
#     //      XML
#     //////////////////////////////////////////
#     /**
#      * <b> XML 파일의 Root Element를 조회 </b>
#      */
#     public static Element getXmlRoot(String xmlFullPath)
#     {
#         return XMLUtils.getRootElm(xmlFullPath);
#     }


#     /**
#      * <b> XML 파일의 첫 Element 목록을 조회 </b>
#      */
#     public static List<Element> getXmlFirstElmList(String xmlFullPath)
#     {
#         return XMLUtils.getFirstElmList(xmlFullPath);
#     }


#     /**
#      * <b> Element List에서 특정 Element를 조회. 첫번째 매치되는 노드를 리턴. </b>
#      */
#     public static Element getXmlElm(List<Element> elmList, String name)
#     {
#         return XMLUtils.getElm(elmList, name);
#     }


#     /**
#      * <b> Element List에서 특정 값을 조회. </b>
#      */
#     public static List<String> getXmlElmValList(List<Element> elmList, String name)
#     {
#         return XMLUtils.getElmValList(elmList, name);
#     }


#     /**
#      * <b> Element List에서 특정 값을 조회. 단, Uniq하지 않으면 오류 발생 </b>
#      */
#     public static String getXmlElmVal(List<Element> elmList, String name) throws Exception
#     {
#         return XMLUtils.getElmVal(elmList, name);
#     }


#     /**
#      * <b> 특정 attribute 값을 조회. 단, Uniq하지 않으면 오류 발생 </b>
#      */
#     public static Attribute getXmlAttribute(Element elm, String name) throws Exception
#     {
#         return XMLUtils.getAttribute(elm, name);
#     }

#     //////////////////////////////////////////
#     //      XXX
#     //////////////////////////////////////////


#     //////////////////////////////////////////
#     //      XXX
#     //////////////////////////////////////////



# }






##########################################
##      LOGGING
##########################################
# 로그 설정값을 관리
class _logger_config:

    def __init__(self):
        ######################
        # 기본 변수

        # 호출자 인덱스
        self._CALLER_IDX        = 4;

        # 문자열 치환자
        self._LOG_SUBSTITUTOR    = "%%";

        # 시스템 로그를 포함하여 출력
        self.DEBUG_LEVEL_ALL    = _logger_util().get_log_level_index("SYSTEM");
        # # DB접근 로그를 포함하여 출력
        self.DEBUG_LEVEL_DB     = _logger_util().get_log_level_index("DB");
        # # 프로그램 로그를 포함하여 출력
        self.DEBUG_LEVEL_DEBUG  = _logger_util().get_log_level_index("DEBUG");
        # # 중요 정보 발생시 출력
        self.DEBUG_LEVEL_INFO   = _logger_util().get_log_level_index("INFO");
        # # 오류 발생시 출력
        self.DEBUG_LEVEL_ERROR  = _logger_util().get_log_level_index("ERROR");


        ######################
        # 설정

        # 파일명 지정
        self.CONFIG_FILE_PATH = ''

        ######################
        # 로거 동작 설정
        ######################
        # 현재 로그레벨 (최초 생성시 기본로그레벨로 세팅)
        self.CURR_DEBUG_LEVEL       = _logger_util().get_log_level_index("INFO");

        # 디버깅 출력 방법 : 콘솔 출력 여부
        self.DEBUG_CONSOLE_PRINT_YN = "Y";

        # 디버깅 출력 방법 : 파일 출력 여부
        self.DEBUG_FILE_PRINT_YN    = "N";


        # 디버깅 출력 방법 : 파일 출력 경로
        from datetime import datetime
        self.DEBUG_FILE_DIR_PATH  = "./logs";
        self.DEBUG_FILE_FILE_NAME  = datetime.now().strftime("%H%M%S") + '.log';




class _logger_util:

    def get_log_level_index(self, level: str) -> int:
        ''' 로깅 레벨 설정 '''
        if level == None:
            return 4
        elif level == "ERROR":
            return 4
        elif level == "INFO":
            return 3
        elif level == "DEBUG":
            return 2
        elif level == "DB":
            return 1
        elif level == "SYSTEM":
            return 0
        return 4

    def nvl_dict(self, d: dict, k: str, nv: str) -> str:

        if (d == None):
            return None

        if (isinstance(d, dict) != True):
            return None

        if (k == None):
            return ''

        #import traceback
        try:
            v = d[k]
        except Exception as e:
            v = nv

        # print (f'v[{v}]')

        return v

    def find_config_file_path(self, start_path: str) -> str:
        ''' logger 설정 파일을 찾는다 '''

        import os

        curr_dir = os.path.dirname(start_path)
        CONFIG_FILE_NAME = 'logger.json'

        config_file_path = ""
        for ii in range(5):
            # print("seeking..[{0}]th : {1}".format(ii, curr_dir))

            if (os.path.isfile(curr_dir + "/" + CONFIG_FILE_NAME) == True):
                config_file_path = os.path.join(curr_dir, CONFIG_FILE_NAME)
                # print("찾았다!", config_file_path)
                break
            else:
                # print("상위로 찾아 올라간다[{0}]->[{1}]".format(curr_dir, os.path.abspath(os.path.join(curr_dir, '..'))))
                # root까지 확인된 경우 : 더이상 찾을 수 없을 때
                if (curr_dir == os.path.abspath(os.path.join(curr_dir, '..'))):
                    # print("못찾았다!")
                    config_file_path = ''
                    # raise Exception(CONFIG_FILE_NAME + " 파일을 찾을 수 없습니다.")
                    break
                else:
                    curr_dir = os.path.abspath(os.path.join(curr_dir, '..'))

        # print("get_config_file_path() -> [{0}]".format(config_file_path))
        return config_file_path

    def parse_config_file(self, config_file_path: str) -> dict():
        ''' logger 설정 파일을 읽어 config 객체로 변환한다 '''

        # 파일이 존재하는가
        import os.path
        if (os.path.isfile(config_file_path) != True):
            return None

        # 파싱하자
        import json
        with open(config_file_path) as _cfp:
            config_json = json.load(_cfp)

        if config_json == None:
            return None

        # config 객체 매핑하자
        parsed_config = _logger_config()

        parsed_config.CONFIG_FILE_PATH = config_file_path

        parsed_config.CURR_DEBUG_LEVEL = self.get_log_level_index(self.nvl_dict(config_json, 'LOG_LEVEL', parsed_config.CURR_DEBUG_LEVEL))
        parsed_config.DEBUG_CONSOLE_PRINT_YN = self.nvl_dict(config_json, 'LOG_CONSOLE_YN', parsed_config.DEBUG_CONSOLE_PRINT_YN)
        parsed_config.DEBUG_FILE_PRINT_YN = self.nvl_dict(config_json, 'LOG_FILE_YN', parsed_config.DEBUG_FILE_PRINT_YN)
        parsed_config.DEBUG_FILE_DIR_PATH = self.nvl_dict(config_json, 'LOG_DIR_PATH', parsed_config.DEBUG_FILE_DIR_PATH)
        parsed_config.DEBUG_FILE_FILE_NAME = self.nvl_dict(config_json, 'LOG_FILE_NAME', parsed_config.DEBUG_FILE_FILE_NAME)

        # print(parsed_config.__dict__)
        return parsed_config





# 로깅 클래스의 기능을 담아놓는다.
class _logging:

    def __init__(self):

        super().__init__()

        # 기본 설정 값
        self.config = _logger_config()



    # 호출자 파일 명
    def _caller_file_name(self) -> str:

        import os, inspect
        caller_file_path = inspect.stack()[self.config._CALLER_IDX][1]

        return os.path.basename(caller_file_path)

    # 호출자 라인번호
    def _caller_file_line(self) -> int:
        import inspect
        return inspect.stack()[self.config._CALLER_IDX][2]


    ##########################################
    ##      log
    ##########################################
    def _gen_substitutor_dummy_string(self, cnt: int) -> str:
        '''Dummy 치환자 문자열 생성'''
        ret = ""

        for ii in range(cnt):
            ret = ret + self.config._LOG_SUBSTITUTOR

        return ret


    def _gen_log_header(self, debug_level) -> str:
        '''[HH24MISS.FFF][CALLER_NAME:LINE5byte]'''

        from datetime import datetime

        header = ""
        if (debug_level == self.config.DEBUG_LEVEL_ALL):
            header = header + "[SYS]"
        elif (debug_level == self.config.DEBUG_LEVEL_DB):
            header = header + "[SQL]"
        elif (debug_level == self.config.DEBUG_LEVEL_DEBUG):
            header = header + "[DBG]"
        elif (debug_level == self.config.DEBUG_LEVEL_INFO):
            header = header + "[INF]"
        elif (debug_level == self.config.DEBUG_LEVEL_ERROR):
            header = header + "[ERR]"

        header = header + " " + "[" + datetime.now().strftime("%H%M%S.%f")[:-3] + "]"                                   # 일시
        header = header + " " + "[" + self._caller_file_name() + ":" + str(self._caller_file_line()).zfill(5) + "]"     # 호출자
        # header = header.ljust(40, " ")                                                                                  # 길이 맞추기

        return header



    def _substitute_string(self, input: str, *args) -> str:

        if input == None:
            return None

        # print ("len", str(len(args)))
        # print (args)
        for ii, arg in enumerate(args):

            idx = 0
            try:
                idx = input.index(self.config._LOG_SUBSTITUTOR)
            except Exception as e:
                break;

            # print (idx)
            if (idx < 0):
                break;

            # print (self.config._LOG_SUBSTITUTOR)
            # print (input, input.replace(self.config._LOG_SUBSTITUTOR, str(arg), 1))
            input = input.replace(self.config._LOG_SUBSTITUTOR, str(arg), 1)

        return input


    def _print_log(self, debug_level, template="", *args):
        '''
        로그처리
        header + debug_strings...
        '''

        # 정합성 체크 : 시스템에 정의된 디버그레벨과 비교하여 로깅처리를 할지 정한다
        if (debug_level == None):
            return

        if (debug_level < self.config.CURR_DEBUG_LEVEL):
            return

        # object를 입력한 경우(예 : Exception) 문자로 변환하여 처리
        template_str = str(template)


        ######################
        # 처리

        # 문자열 치환
        log_body = self._substitute_string(template_str, *args)

        # 남은 치환자 제거
        log_body = log_body.replace(self.config._LOG_SUBSTITUTOR, "")


        #################
        # CONSOLE PRINT
        if self.config.DEBUG_CONSOLE_PRINT_YN == "Y":
            print (self._gen_log_header(debug_level) + " " + log_body)


        #################
        # FILE PRINT
        if self.config.DEBUG_FILE_PRINT_YN == "Y":
            print("파일프린트 시작한다[{}]".format(self.config.DEBUG_FILE_PRINT_PATH))
            # writelog (_gen_log_header(debug_level) + " " + log_body)
            pass



######################
# logger 클래스 메인
#   1. 설정파일을 찾아 적용한다. 없으면 기본값으로 적용한다.
class logger(_logging):
    '''
    My favorite log format maker.
    [LEVEL] [TIME] [SOURCE] contents...

    sample>
        logger = krutils.logger(__file__)

        a = 10.0
        b = 20.0

        logger.syslog("[%%] %% - {%%}", a, b, a)
        logger.dblog("[%%] %% - {%%}", a, b, a)
        logger.debug("[%%] %% - {%%}", a, b, a)
        logger.info("[%%] %% - {%%}", a, b, a)
        logger.error("[%%] %% - {%%}", a, b, a)

    result>
        [SYS] [103350.469] [tester.py:00010] [10.0] 20.0 - {10.0}
        [SQL] [103350.512] [tester.py:00011] [10.0] 20.0 - {10.0}
        [DBG] [103350.515] [tester.py:00012] [10.0] 20.0 - {10.0}
        [INF] [103350.518] [tester.py:00013] [10.0] 20.0 - {10.0}
        [ERR] [103350.520] [tester.py:00014] [10.0] 20.0 - {10.0}


    Options>
        Set option can redefine with 'logger.json' file.
        The 'logger.json' file can be caller program directory or above. krutil.logger will seek the 'logger.json' file from caller program directory to root diredctory.
        First found file will be adapted.

        SAMPLE> 'logger.json'
        {
            "__KEYWORDS__" : "LOG_LEVEL/LOG_CONSOLE_YN/LOG_FILE_YN/LOG_DIR_PATH/LOG_FILE_NAME",
            "__LOG_LEVEL__" : "SYSTEM/DB/DEBUG/INFO/ERROR",
            "LOG_LEVEL" : "INFO",
            "LOG_CONSOLE_YN" : "Y",
            "LOG_FILE_YN" : "N",
            "LOG_DIR_PATH" : "./logs",
            "LOG_FILE_NAME" : "mylog.log"
        }

        DESC> * is default value
        * LOG_LEVEL : SYSTEM/DB/DEBUG/INFO*/ERROR
        * LOG_CONSOLE_YN : Y*/N
        * LOG_FILE_YN : Y/N*
        * LOG_DIR_PATH : log directory path(None is default)
        * LOG_FILE_NAME : log file name(None is default)

    '''

    def __init__(self, caller_path: str):

        # logger에 필요한 변수와 기능이 담겨있는 super 클래스를 초기화 한다.
        super().__init__()

        # 인자로 받은 호출자 경로로 부터 root까지 탐색하며 config 파일을 찾는다.
        # 존재시 설정을 덮어 씌운다
        cfp = _logger_util().find_config_file_path(caller_path)

        if (is_empty(cfp) != True):
            parsed_config = _logger_util().parse_config_file(cfp)

            if (parsed_config != None):
                self.config = parsed_config
                self.config.CONFIG_FILE_PATH = cfp


    def syslog(self, template="", *args):
        self._print_log(self.config.DEBUG_LEVEL_ALL, template, *args)



    def dblog(self, template="", *args):
        self._print_log(self.config.DEBUG_LEVEL_DB, template, *args)



    def debug(self, template="", *args):
        self._print_log(self.config.DEBUG_LEVEL_DEBUG, template, *args)



    def info(self, template="", *args):
        self._print_log(self.config.DEBUG_LEVEL_INFO, template, *args)



    def error(self, template="", *args):
        self._print_log(self.config.DEBUG_LEVEL_ERROR, template, *args)



















