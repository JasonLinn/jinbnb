// 多語言切換功能
const translations = {
  'zh-TW': {
    // 導航欄
    'nav-home': '首頁',
    'nav-posts': '最新消息',
    'nav-booking': '官網優惠訂房',
    'nav-line': 'LINE加入好友',

    // 標題
    'news-title': '最新消息',
    'env-title': '民宿環境',
    'a-room-title': 'A棟套房',
    'b-room-title': 'B棟套房',
    'a-full-title': 'A棟包棟價格',
    'notice-title': '入住須知',
    'service-title': '貼心服務',
    'contact-title': '聯絡資訊',
    'other-title': '其他',
    'location-title': '位置',

    // 標籤和按鈕
    'notice-header': '入住須知',
    'cancel-header': '取消訂房退款',
    'payment-header': '匯款資訊',
    'bike-service': '自行車租車優惠',
    'bbq-service': '烤肉、外燴代訂',
    'tour-service': '遊程代訂',

    // 聯絡資訊
    'phone-label': '訂房專線:',
    'line-label': 'LINE:',

    // 頁腳
    'footer-text': '衿日林民宿 All Rights Reserved.',

    // 輪播標題
    'carousel-bbq': '烤肉趴',
    'carousel-outside': '民宿外觀',
    'carousel-birthday': '蜜月雙人房生日佈置',

    // 民宿環境圖片說明
    'env-outside': '外觀',
    'env-restaurant': '餐廳',
    'env-living': 'A棟客廳',
    'env-bbq': 'A棟烤肉區(包棟開放)',
    'env-pool': 'A棟戲水池(包棟開放)',
    'env-slide': '兒童溜滑梯',

    // A棟套房
    'room-mini': '迷你雙人房',
    'room-style': '風格雙人房',
    'room-twin': '雙床雙人房',
    'room-family': '親子四人房',
    'room-quad': '巧巧四人房',
    'room-bath': '浴廁',

    // B棟套房
    'room-honey': '度假蜜月雙人房',
    'room-romantic': '浪漫蜜月雙人房',
    'room-wedding': '花嫁四人房',

    // 服務項目
    'service-bike': '合作店家吉美、親親自行車租車優惠，悠遊冬山河畔，深度旅遊攻略：',
    'service-bbq-1': '1.烤肉套餐，烤肉車',
    'service-bbq-2': '2.火鍋套餐',
    'service-bbq-3': '3.派對調酒車',
    'service-bbq-4': '4.在地合菜',
    'service-bbq-5': '5.生日佈置',
    'service-tour-1': '1.龜山島賞鯨',
    'service-tour-2': '2.冬山河SUP、獨木舟',
    'service-tour-3': '3.南方澳SUP',
    'service-tour-4': '4.三星上將溪泛舟',
    'service-tour-5': '5.安永心食館(觀光工廠)優惠入園',

    // 入住須知
    'notice-1': '1. 進房時間15：00後，退房隔日11：00前。',
    'notice-2': '2. 全館禁菸，如需吸菸請至本棟建築物外。',
    'notice-3': '3. 晚上22：00後請降低音量。',
    'notice-4': '4. 部分房型可加床，請事先告知，800/一床',

    // 新增：最新消息
    'news-2024-ciff-title': '2024童玩節即將登場',
    'news-2024-ciff-time': '🚀活動時間7/6~8/18',
    'news-2024-ciff-location': '衿日林民宿離會場步行僅一分鐘',
    'news-2024-ciff-rooms': '多種平價套房任選',

    'news-redbean-title': '包棟贈紅豆湯圓',
    'news-redbean-date': '👉 即日起至 113年1月31日',
    'news-redbean-gift': '👉 包棟入住即獲贈一鍋 #暖心的紅豆湯圓 😍',
    'news-redbean-intro': '👉 衿日林民宿 誠摯邀您包棟享受專屬空間，無論是家庭聚會或好友相聚，我們提供獨特體驗，讓您感受滿滿溫暖與溫馨。',
    'news-redbean-features': '👉 獨享:',
    'news-redbean-feature-1': '#庭院烤肉場地',
    'news-redbean-feature-2': '#卡拉OK',
    'news-redbean-feature-3': '#電動麻將',
    'news-redbean-feature-4': '#中式早餐',

    // 網站資訊
    'site-title': '宜蘭衿日林民宿|官方網站|童玩節正對面|YilanB&B',
    'site-description': '宜蘭衿日林獨棟/包棟民宿，冬山河親水公園，童玩節會場正對面，提供平價套房、早餐、免費大型停車場(可停遊覽車)，適合烤肉、唱歌、親子騎自行車，近傳統藝術中心、羅東夜市、三奇美徑。宜蘭出差首選、平價套房、交通方便。',
    'brand-name': '宜蘭衿日林民宿',

    // 2025童玩節新聞
    'news-2025-ciff-title': '2025宜蘭國際童玩節預售票開賣',
    'news-2025-ciff-date': '2025/5/1',
    'news-2025-ciff-intro': '🎉 2025宜蘭國際童玩藝術節即將於7月5日至8月17日在冬山河親水公園舉行',
    'news-2025-ciff-time': '⏰ 每天開放時間：上午9點至晚上9點',
    'news-2025-ciff-price-title': '💰 票價資訊：',
    'news-2025-ciff-regular-price': '一般票價：',
    'news-2025-ciff-weekday': '- 平日券 250元',
    'news-2025-ciff-weekend': '- 假日券 350元',
    'news-2025-ciff-presale': '預售優惠票價（5/1-7/4）：',
    'news-2025-ciff-presale-weekday': '- 平日券 200元（省50元）',
    'news-2025-ciff-presale-weekend': '- 假日券 300元（省50元）',
    'news-2025-ciff-channel': '🎫 購票管道：',
    'news-2025-ciff-channel-711': '- 7-11超商ibon機台',
    'news-2025-ciff-channel-klook': '- Klook線上平台',
    'news-2025-ciff-special': '✨ 特別優惠：',
    'news-2025-ciff-combo': '🌟 童玩傳藝雙園區套票（含兩張園區門票及傳藝150元精選手作課程）',
    'news-2025-ciff-combo-weekday': '- 平日券 450元',
    'news-2025-ciff-combo-weekend': '- 假日券 550元',
    'news-2025-ciff-transport': '🌟 大眾運輸優惠：搭乘指定客運可享優惠票價',
    'news-2025-ciff-transport-weekday': '- 平日券 200元',
    'news-2025-ciff-transport-weekend': '- 假日券 300元',
    'news-2025-ciff-card': '🌟 第一銀行宜蘭認同卡優惠（每日一卡限4張）',
    'news-2025-ciff-card-weekday': '- 平日券 200元',
    'news-2025-ciff-card-weekend': '- 假日券 300元',
    'news-2025-ciff-night': '🌙 星光票特惠：',
    'news-2025-ciff-night-price': '- 票價：100元',
    'news-2025-ciff-night-time': '- 購買時間：每天下午6點至7點現場購票',
    'news-2025-ciff-night-feature': '- 特色：欣賞世界各國民俗團隊表演、全區遊藝踩街、夢幻水舞燈光秀',
    'news-2025-ciff-location': '📍 衿日林民宿位於童玩節會場正對面，步行僅需1分鐘！',
    'news-2025-ciff-more': '🔍 更多票價資訊請上「2025宜蘭國際童玩藝術節」網站查詢：',
  },
  'en': {
    // 導航欄
    'nav-home': 'Home',
    'nav-posts': 'All Posts',
    'nav-booking': 'Book Online',
    'nav-line': 'Add LINE Friend',

    // 標題
    'news-title': 'Latest News',
    'env-title': 'B&B Environment',
    'a-room-title': 'Building A Rooms',
    'b-room-title': 'Building B Rooms',
    'a-full-title': 'Building A Full Rental Prices',
    'notice-title': 'Stay Information',
    'service-title': 'Services',
    'contact-title': 'Contact Information',
    'other-title': 'Others',
    'location-title': 'Location',

    // 標籤和按鈕
    'notice-header': 'Check-in Information',
    'cancel-header': 'Cancellation Policy',
    'payment-header': 'Payment Information',
    'bike-service': 'Bicycle Rental',
    'bbq-service': 'BBQ & Catering',
    'tour-service': 'Tour Booking',

    // 聯絡資訊
    'phone-label': 'Reservation Line:',
    'line-label': 'LINE:',

    // 頁腳
    'footer-text': 'Jin B&B All Rights Reserved.',

    // 輪播標題
    'carousel-bbq': 'BBQ Party',
    'carousel-outside': 'B&B Exterior',
    'carousel-birthday': 'Honeymoon Room Birthday Decoration',

    // 民宿環境圖片說明
    'env-outside': 'Exterior',
    'env-restaurant': 'Restaurant',
    'env-living': 'Building A Living Room',
    'env-bbq': 'Building A BBQ Area (Full Rental Only)',
    'env-pool': 'Building A Pool (Full Rental Only)',
    'env-slide': 'Children\'s Slide',

    // A棟套房
    'room-mini': 'Mini Double Room',
    'room-style': 'Style Double Room',
    'room-twin': 'Twin Bed Room',
    'room-family': 'Family Quad Room',
    'room-quad': 'Cozy Quad Room',
    'room-bath': 'Bathroom',

    // B棟套房
    'room-honey': 'Vacation Honeymoon Room',
    'room-romantic': 'Romantic Honeymoon Room',
    'room-wedding': 'Wedding Quad Room',

    // 服務項目
    'service-bike': 'Discounted bicycle rentals at partner shops Jimi and Qinqin. Enjoy cycling along the Dongshan River. Travel guide:',
    'service-bbq-1': '1. BBQ packages and BBQ cart',
    'service-bbq-2': '2. Hot pot packages',
    'service-bbq-3': '3. Party cocktail cart',
    'service-bbq-4': '4. Local cuisine',
    'service-bbq-5': '5. Birthday decorations',
    'service-tour-1': '1. Turtle Island whale watching',
    'service-tour-2': '2. Dongshan River SUP, canoe',
    'service-tour-3': '3. Nanfang\'ao SUP',
    'service-tour-4': '4. Sanxing River rafting',
    'service-tour-5': '5. An-Yong Heart Food Museum (tourist factory) discounted admission',

    // 入住須知
    'notice-1': '1. Check-in after 15:00, check-out before 11:00 the next day.',
    'notice-2': '2. No smoking inside the building. Please smoke outside the building.',
    'notice-3': '3. Please lower the volume after 22:00.',
    'notice-4': '4. Extra beds are available for some room types, please inform in advance, NT$800 per bed.',

    // New: Latest News
    'news-2024-ciff-title': '2024 Children\'s Folklore Festival Coming Soon',
    'news-2024-ciff-time': '🚀Event Period: July 6 - August 18',
    'news-2024-ciff-location': 'Only 1-minute walk from the venue',
    'news-2024-ciff-rooms': 'Various affordable room types available',

    'news-redbean-title': 'Free Red Bean Tangyuan with Full House Booking',
    'news-redbean-date': '👉 From now until January 31, 2024',
    'news-redbean-gift': '👉 Get a complimentary pot of #heartwarming red bean tangyuan with full house booking 😍',
    'news-redbean-intro': '👉 Jin B&B sincerely invites you to enjoy our exclusive space. Whether for family gatherings or friend reunions, we offer unique experiences filled with warmth and comfort.',
    'news-redbean-features': '👉 Exclusive access to:',
    'news-redbean-feature-1': '#Garden BBQ Area',
    'news-redbean-feature-2': '#Karaoke',
    'news-redbean-feature-3': '#Electric Mahjong',
    'news-redbean-feature-4': '#Chinese Breakfast',

    // Website Info
    'site-title': 'Yilan Jin B&B|Official Website|Opposite to Children\'s Festival|YilanB&B',
    'site-description': 'Yilan Jin B&B exclusive/full-house rental, opposite to Dongshan River Water Park and Children\'s Festival venue. Offering affordable suites, breakfast, free large parking (suitable for tour buses). Perfect for BBQ, karaoke, family cycling. Near National Center for Traditional Arts, Luodong Night Market, and Sanqi Trail.',
    'brand-name': 'Yilan Jin B&B',

    // 2025 Children's Festival News
    'news-2025-ciff-title': '2025 Yilan International Children\'s Folklore & Folkgame Festival Presale Tickets Available',
    'news-2025-ciff-date': 'May 1, 2025',
    'news-2025-ciff-intro': '🎉 The 2025 Yilan International Children\'s Folklore & Folkgame Festival will be held at Dongshan River Water Park from July 5 to August 17',
    'news-2025-ciff-time': '⏰ Opening Hours: 9:00 AM to 9:00 PM daily',
    'news-2025-ciff-price-title': '💰 Ticket Information:',
    'news-2025-ciff-regular-price': 'Regular Price:',
    'news-2025-ciff-weekday': '- Weekday Ticket NT$250',
    'news-2025-ciff-weekend': '- Weekend Ticket NT$350',
    'news-2025-ciff-presale': 'Presale Price (May 1 - July 4):',
    'news-2025-ciff-presale-weekday': '- Weekday Ticket NT$200 (Save NT$50)',
    'news-2025-ciff-presale-weekend': '- Weekend Ticket NT$300 (Save NT$50)',
    'news-2025-ciff-channel': '🎫 Where to Buy:',
    'news-2025-ciff-channel-711': '- 7-11 ibon Kiosk',
    'news-2025-ciff-channel-klook': '- Klook Online Platform',
    'news-2025-ciff-special': '✨ Special Offers:',
    'news-2025-ciff-combo': '🌟 Festival & NCFTA Combo Ticket (Includes two festival tickets and NT$150 NCFTA DIY workshop)',
    'news-2025-ciff-combo-weekday': '- Weekday Ticket NT$450',
    'news-2025-ciff-combo-weekend': '- Weekend Ticket NT$550',
    'news-2025-ciff-transport': '🌟 Public Transport Discount: Special price for designated bus passengers',
    'news-2025-ciff-transport-weekday': '- Weekday Ticket NT$200',
    'news-2025-ciff-transport-weekend': '- Weekend Ticket NT$300',
    'news-2025-ciff-card': '🌟 First Bank Yilan Card Holder Discount (Limited to 4 tickets per card per day)',
    'news-2025-ciff-card-weekday': '- Weekday Ticket NT$200',
    'news-2025-ciff-card-weekend': '- Weekend Ticket NT$300',
    'news-2025-ciff-night': '🌙 Night Ticket Special:',
    'news-2025-ciff-night-price': '- Price: NT$100',
    'news-2025-ciff-night-time': '- Available: 6:00 PM to 7:00 PM daily at the venue',
    'news-2025-ciff-night-feature': '- Features: International folk performances, parade, and spectacular water and light show',
    'news-2025-ciff-location': '📍 Jin B&B is just 1-minute walk from the festival venue!',
    'news-2025-ciff-more': '🔍 For more ticket information, please visit the 2025 Yilan International Children\'s Folklore & Folkgame Festival website:',
  }
};

// 默認語言
let currentLang = 'zh-TW';

// 切換語言函數
function switchLanguage(lang) {
  if (!translations[lang]) return;

  currentLang = lang;

  // 儲存語言選擇到 localStorage
  localStorage.setItem('preferred_language', lang);

  // 更新所有帶有 data-i18n 屬性的元素
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    if (translations[lang][key]) {
      element.textContent = translations[lang][key];
    }
  });

  // 更新語言切換按鈕狀態
  document.querySelectorAll('.language-btn').forEach(btn => {
    if (btn.getAttribute('data-lang') === lang) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // 更新 HTML 語言屬性
  document.documentElement.lang = lang;
}

// 初始化語言設定
document.addEventListener('DOMContentLoaded', () => {
  // 檢查是否有儲存的語言選擇
  const savedLang = localStorage.getItem('preferred_language');
  if (savedLang && translations[savedLang]) {
    switchLanguage(savedLang);
  } else {
    // 檢查瀏覽器語言
    const browserLang = navigator.language || navigator.userLanguage;
    if (browserLang.includes('zh')) {
      switchLanguage('zh-TW');
    } else {
      switchLanguage('en');
    }
  }

  // 為語言切換按鈕添加事件監聽器
  document.querySelectorAll('.language-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const lang = btn.getAttribute('data-lang');
      switchLanguage(lang);
    });
  });
}); 