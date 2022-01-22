from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


options = ChromeOptions()
options.headless = True
driver = Chrome(options=options)
driver.get('https://opensea.io')

html = driver.execute_script("return document.documentElement.outerHTML")

# print(html)

soup = BeautifulSoup(html, 'html.parser')

print(soup.select('.Blockreact__Block-sc-1xf18x6-0'))




# //*[@id="main"]/div/div[2]/section/section/div[2]/div/div/a[1]/div[3]/span[1]/div

# collections = driver.find_element(By.CLASS_NAME, 'glymPt')

# for collection in collections:
#     title = collection.text

# # title = [link.text for link in collections]
# print(collections)

driver.quit()

'''
<a class="styles__StyledLink-sc-l6elh8-0 ekTmzq Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 Itemreact__ItemBase-sc-1idymv7-0 fHytVd jYqxGr glymPt TopCollections--item" height="88" href="/collection/cryptopunks">
<div class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 CenterAlignedreact__CenterAligned-sc-cjf6mn-0 ePfTsZ jYqxGr ksFzlZ iXcsEj cgnEmv">
<span font-size="16px" class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 hkPSPS kCOfJW"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf">3</div>
</span></div><div class="Blockreact__Block-sc-1xf18x6-0 bLjycD"><div class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 bmYtOF jYqxGr">
<div class="Imagereact__DivContainer-sc-dy59cl-0 hezVSt Image--isImageLoaded Image--isImageLoaderVisible" style="height: 50px; width: 50px;">
<img alt="" class="Image--image" src="https://lh3.googleusercontent.com/BdxvLseXcfl57BiuQcQYdJ64v-aI8din7WPk0Pgo3qQFhAUH-B6i-dCqqc_mCkRIzULmwzwecnohLhrcH8A9mpWIZqA7ygc52Sr81hE=s100" style="object-fit: cover;">
</div></div><div class="Blockreact__Block-sc-1xf18x6-0 CollectionAvatarreact__VerifiedIndicator-sc-3iovjc-1 dBFmez hnMxMS"><svg class="VerifiedIconreact__StyledSvg-sc-50keu7-0 ljSZXh" fill="none" viewBox="0 0 30 30">
<path class="VerifiedIcon--background" d="M13.474 2.80108C14.2729 1.85822 15.7271 1.85822 16.526 2.80108L17.4886 3.9373C17.9785 4.51548 18.753 4.76715 19.4892 4.58733L20.9358 4.23394C22.1363 3.94069 23.3128 4.79547 23.4049 6.0278L23.5158 7.51286C23.5723 8.26854 24.051 8.92742 24.7522 9.21463L26.1303 9.77906C27.2739 10.2474 27.7233 11.6305 27.0734 12.6816L26.2903 13.9482C25.8918 14.5928 25.8918 15.4072 26.2903 16.0518L27.0734 17.3184C27.7233 18.3695 27.2739 19.7526 26.1303 20.2209L24.7522 20.7854C24.051 21.0726 23.5723 21.7315 23.5158 22.4871L23.4049 23.9722C23.3128 25.2045 22.1363 26.0593 20.9358 25.7661L19.4892 25.4127C18.753 25.2328 17.9785 25.4845 17.4886 26.0627L16.526 27.1989C15.7271 28.1418 14.2729 28.1418 13.474 27.1989L12.5114 26.0627C12.0215 25.4845 11.247 25.2328 10.5108 25.4127L9.06418 25.7661C7.86371 26.0593 6.6872 25.2045 6.59513 23.9722L6.48419 22.4871C6.42773 21.7315 5.94903 21.0726 5.24777 20.7854L3.86969 20.2209C2.72612 19.7526 2.27673 18.3695 2.9266 17.3184L3.70973 16.0518C4.10824 15.4072 4.10824 14.5928 3.70973 13.9482L2.9266 12.6816C2.27673 11.6305 2.72612 10.2474 3.86969 9.77906L5.24777 9.21463C5.94903 8.92742 6.42773 8.26854 6.48419 7.51286L6.59513 6.0278C6.6872 4.79547 7.86371 3.94069 9.06418 4.23394L10.5108 4.58733C11.247 4.76715 12.0215 4.51548 12.5114 3.9373L13.474 2.80108Z"></path><path d="M13.5 17.625L10.875 15L10 15.875L13.5 19.375L21 11.875L20.125 11L13.5 17.625Z" fill="white" stroke="white">
</path></svg></div></div><div class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 Itemreact__ItemContent-sc-1idymv7-1 dBFmez jYqxGr ksFzlZ iXcsEj hTefVc">
<span width="100%" font-size="14px" class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 Itemreact__ItemTitle-sc-1idymv7-2 RrSDj ibqWjk"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf">CryptoPunks</div></span><span class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 Itemreact__ItemDescription-sc-1idymv7-6 dBFmez gwsEKa">
<div class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 gctoET jYqxGr"><div display="inline-flex" height="22px" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 hEuIQn jYqxGr">
<div cursor="pointer" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 CenterAlignedreact__CenterAligned-sc-cjf6mn-0 kTFrxw jYqxGr ksFzlZ iXcsEj cgnEmv">
<div size="14" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 CenterAlignedreact__CenterAligned-sc-cjf6mn-0 Avatarreact__AvatarContainer-sc-sbw25j-0 hkQgWj jYqxGr ksFzlZ iXcsEj cgnEmv dukFGY">
<img src="https://storage.opensea.io/files/6f8e2979d428180222796ff4a33ab929.svg" class="Blockreact__Block-sc-1xf18x6-0 Avatarreact__ImgAvatar-sc-sbw25j-1 hkQgWj hzWBaN EthLogoreact__EthAvatar-sc-bgaajd-0" size="14">
</div></div></div><span color="#8A939B" font-size="14px" font-weight="600" class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 styles__StatText-sc-12irlp3-3 bYMNtJ jOSRNl">
<div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf">10 211,35</div></span></div></span></div><div class="Blockreact__Block-sc-1xf18x6-0 Itemreact__ItemSide-sc-1idymv7-3 dBFmez cDmIYg">
<div class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 dBFmez jYqxGr"><span color="coral" font-weight="400" font-size="[object Object]" class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 styles__StatText-sc-12irlp3-3 jQuHmJ bBZra">
<div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf">-5.87%</div></span></div></div></a>
'''