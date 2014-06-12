# The Grinder 3.11
# HTTP script recorded by TCPProxy at May 29, 2014 3:12:48 PM

import os
from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

SECURE = os.getenv('LOAD_SECURE', "yes") == "yes"
PROTOCOL = ('https' if SECURE else 'http')
APP_HOST = os.getenv('LOAD_APP_HOST', 'forio.com')
APP_ACCOUNT = os.getenv('LOAD_APP_ACCOUNT', 'showcase')
APP_PROJECT = os.getenv('LOAD_APP_PROJECT', 'route-optimizer')
APP_PATH = APP_ACCOUNT + '/' + APP_PROJECT
API_HOST = os.getenv('LOAD_API_HOST', 'api.forio.com')
STATIC_URL = PROTOCOL + '://' + APP_HOST

staticHeaders = [
  NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
  NVPair('Accept-Encoding', 'gzip,deflate,sdch'),
  NVPair('Accept-Language', 'en-US,en;q=0.8'),
  NVPair('Cache-Control', 'no-cache'),
  NVPair('Pragma', 'no-cache'),
  NVPair('Host', APP_HOST),
  NVPair('Referer', STATIC_URL),
  NVPair('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'),
  NVPair('Connection', 'keep-alive')
]

def createRequest(test, url, headers=staticHeaders):
    """Create an instrumented HTTPRequest."""
    request = HTTPRequest(url=url)
    if headers: request.headers=headers
    test.record(request, HTTPRequest.getHttpMethodFilter())
    return request

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

url0 = STATIC_URL

request101 = createRequest(Test(101, 'GET /'), url0)

request102 = createRequest(Test(102, 'GET jquery.min.js'), url0)

request103 = createRequest(Test(103, 'GET lodash.min.js'), url0)

request104 = createRequest(Test(104, 'GET d3.min.js'), url0)

request105 = createRequest(Test(105, 'GET backbone.js'), url0)

request106 = createRequest(Test(106, 'GET contour.min.js'), url0)

request107 = createRequest(Test(107, 'GET app.js'), url0)

request108 = createRequest(Test(108, 'GET main.css'), url0)

request201 = createRequest(Test(201, 'GET epicenter-logo.svg'), url0)

request301 = createRequest(Test(301, 'GET mandelbrot-logo.svg'), url0)

request401 = createRequest(Test(401, 'GET contour-logo.svg'), url0)

request501 = createRequest(Test(501, 'GET julia.svg'), url0)

request601 = createRequest(Test(601, 'GET opensource-logo.svg'), url0)

request701 = createRequest(Test(701, 'GET map.svg'), url0)

request801 = createRequest(Test(801, 'GET logo-white.svg'), url0)

request901 = createRequest(Test(901, 'GET logo.svg'), url0)

request1001 = createRequest(Test(1001, 'GET book-crawl.json'), url0)

request1101 = createRequest(Test(1101, 'GET ss-symbolicons-block.woff'), url0)

request1102 = createRequest(Test(1102, 'GET marker-sprite-shadow.png'), url0)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET / (requests 101-108)."""
    result = request101.GET('/app/' + APP_PATH)
    self.token_family = \
      httpUtilities.valueFromBodyURI('family') # 'Open+Sans:300'

    grinder.sleep(173)
    request102.GET('/app/' + APP_PATH + '/vendor/jquery/dist/jquery.min.js')

    request103.GET('/app/' + APP_PATH + '/vendor/lodash/dist/lodash.min.js')

    request104.GET('/app/' + APP_PATH + '/vendor/d3/d3.min.js')

    request105.GET('/app/' + APP_PATH + '/vendor/backbone/backbone.js')

    request106.GET('/app/' + APP_PATH + '/vendor/contour/dist/contour.min.js')

    request107.GET('/app/' + APP_PATH + '/scripts/app.js')

    grinder.sleep(68)
    request108.GET('/app/' + APP_PATH + '/styles/main.css')

    return result

  def page2(self):
    """GET epicenter-logo.svg (request 201)."""
    result = request201.GET('/app/' + APP_PATH + '/styles/assets/logos/epicenter-logo.svg')

    return result

  def page3(self):
    """GET mandelbrot-logo.svg (request 301)."""
    result = request301.GET('/app/' + APP_PATH + '/styles/assets/logos/mandelbrot-logo.svg')

    return result

  def page4(self):
    """GET contour-logo.svg (request 401)."""
    result = request401.GET('/app/' + APP_PATH + '/styles/assets/logos/contour-logo.svg')

    return result

  def page5(self):
    """GET julia.svg (request 501)."""
    result = request501.GET('/app/' + APP_PATH + '/styles/assets/logos/julia.svg')

    return result

  def page6(self):
    """GET opensource-logo.svg (request 601)."""
    result = request601.GET('/app/' + APP_PATH + '/styles/assets/logos/opensource-logo.svg')

    return result

  def page7(self):
    """GET map.svg (request 701)."""
    result = request701.GET('/app/' + APP_PATH + '/styles/assets/logos/map.svg')

    return result

  def page8(self):
    """GET logo-white.svg (request 801)."""
    result = request801.GET('/app/' + APP_PATH + '/styles/assets/logo-white.svg')

    return result

  def page9(self):
    """GET logo.svg (request 901)."""
    result = request901.GET('/app/' + APP_PATH + '/styles/assets/logo.svg')

    return result

  def page10(self):
    """GET book-crawl.json (request 1001)."""
    result = request1001.GET('/app/' + APP_PATH + '/data/book-crawl.json')

    return result

  def page11(self):
    """GET ss-symbolicons-block.woff (requests 1101-1102)."""
    result = request1101.GET('/app/' + APP_PATH + '/styles/assets/fonts/symbolicons/ss-symbolicons-block.woff')

    grinder.sleep(715)
    request1102.GET('/app/' + APP_PATH + '/styles/assets/marker-sprite-shadow.png')

    return result

  def __call__(self):
    """Called for every run performed by the worker thread."""
    self.page1()      # GET / (requests 101-108)

    grinder.sleep(243)
    self.page2()      # GET epicenter-logo.svg (request 201)
    self.page3()      # GET mandelbrot-logo.svg (request 301)
    self.page4()      # GET contour-logo.svg (request 401)
    self.page5()      # GET julia.svg (request 501)
    self.page6()      # GET opensource-logo.svg (request 601)
    self.page7()      # GET map.svg (request 701)
    self.page8()      # GET logo-white.svg (request 801)
    self.page9()      # GET logo.svg (request 901)
    self.page10()     # GET book-crawl.json (request 1001)

    grinder.sleep(149)
    self.page11()     # GET ss-symbolicons-block.woff (requests 1101-1102)


# Instrument page methods.
Test(100, 'Page 1').record(TestRunner.page1)
Test(200, 'Page 2').record(TestRunner.page2)
Test(300, 'Page 3').record(TestRunner.page3)
Test(400, 'Page 4').record(TestRunner.page4)
Test(500, 'Page 5').record(TestRunner.page5)
Test(600, 'Page 6').record(TestRunner.page6)
Test(700, 'Page 7').record(TestRunner.page7)
Test(800, 'Page 8').record(TestRunner.page8)
Test(900, 'Page 9').record(TestRunner.page9)
Test(1000, 'Page 10').record(TestRunner.page10)
Test(1100, 'Page 11').record(TestRunner.page11)