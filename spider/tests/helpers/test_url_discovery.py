import scrapy
import json

from spider.luxonis_crawler.spiders.helpers import url_discovery


def test_url_discovery():
    data_file_path = 'spider/tests/helpers/data/test_url_discovery.json'
    with open(data_file_path, 'r') as file:
        data = json.load(file)

    expected = data["expected"]
    response = scrapy.http.HtmlResponse(url="https://www.sreality.cz/en/search/for-sale/houses",
                                        encoding="utf-8",
                                        body="""
    <div ng-if="pagingData" class="paging ng-scope" paging="paging">
        <ul class="paging-full">
            <li class="paging-item">
                <a ng-href="" class="btn-paging-pn icof icon-arr-left paging-prev disabled" ng-class="{disabled: !pagingData.prevUrl}"></a>
            </li>
            <!--
         -->
            <!-- ngRepeat: page in pagingData.pagesFull --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesFull" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses" ng-class="{active: page.active}" class="btn-paging ng-binding active" href="/en/search/for-sale/houses" cgqwssnkn="">1</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesFull --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesFull" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=2" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=2" cgqwssnkn="">2</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesFull --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesFull" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=3" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=3" cgqwssnkn="">3</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesFull --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesFull" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=4" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=4" cgqwssnkn="">4</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesFull --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesFull" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=5" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=5" cgqwssnkn="">5</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesFull --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesFull" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=6" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=6" cgqwssnkn="">6</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesFull --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesFull" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=7" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=7" cgqwssnkn="">7</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesFull --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesFull" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=8" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=8" cgqwssnkn="">8</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesFull --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesFull" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=9" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=9" cgqwssnkn="">9</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesFull --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesFull" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=10" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=10" cgqwssnkn="">10</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesFull -->
            <!--
         -->
            <li class="paging-item">
                <a ng-href="/en/search/for-sale/houses?page=2" class="btn-paging-pn icof icon-arr-right paging-next" ng-class="{disabled: !pagingData.nextUrl}" href="/en/search/for-sale/houses?page=2" cgqwssnkn=""></a>
            </li>
        </ul>
    
        <ul class="paging-small">
            <li class="paging-item">
                <a ng-href="" class="btn-paging-pn icof icon-arr-left paging-prev disabled" ng-class="{disabled: !pagingData.prevUrl}"></a>
            </li>
            <!--
         -->
            <!-- ngRepeat: page in pagingData.pagesSmall --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesSmall" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses" ng-class="{active: page.active}" class="btn-paging ng-binding active" href="/en/search/for-sale/houses" cgqwssnkn="">1</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesSmall --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesSmall" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=2" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=2" cgqwssnkn="">2</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesSmall --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesSmall" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=3" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=3" cgqwssnkn="">3</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesSmall --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesSmall" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=4" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=4" cgqwssnkn="">4</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesSmall --><li class="paging-item ng-scope" ng-repeat="page in pagingData.pagesSmall" ng-class="{'dots-after': page.dotsAfter}">
                <a ng-href="/en/search/for-sale/houses?page=5" ng-class="{active: page.active}" class="btn-paging ng-binding" href="/en/search/for-sale/houses?page=5" cgqwssnkn="">5</a><!--
         -->
            </li><!-- end ngRepeat: page in pagingData.pagesSmall -->
            <!--
         -->
            <li class="paging-item">
                <a ng-href="/en/search/for-sale/houses?page=2" class="btn-paging-pn icof icon-arr-right paging-next" ng-class="{disabled: !pagingData.nextUrl}" href="/en/search/for-sale/houses?page=2" cgqwssnkn=""></a>
            </li>
        </ul>
    
        <p class="info ng-binding">
            Results
            <span class="numero ng-binding">1–20</span>
            from the amout
            <span class="numero ng-binding">17&nbsp;743</span>&nbsp;of found estates
        </p>
    </div>
    """)

    res = url_discovery.extract_urls(response)
    assert res == expected