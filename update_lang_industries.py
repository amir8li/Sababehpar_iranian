import re

with open('lang.js', 'r') as f:
    content = f.read()

# 1. Update the 'en' dictionary
en_updates = """
    'industry-paint-title': 'Paint & Resin',
    'industry-paint-text': 'Essential mineral filler for paints and industrial coatings.',
    'industry-plastics-title': 'Plastics & Polymers',
    'industry-plastics-text': 'High-quality filler for masterbatches and polymer compounds.',
    'industry-pvc-title': 'PVC, UPVC & Profiles',
    'industry-pvc-text': 'Crucial ingredient for window profiles, wall panels, and flooring.',
    'industry-paper-title': 'Paper & Cardboard',
    'industry-paper-text': 'Improves whiteness, surface uniformity, and printability.',
    'industry-feed-title': 'Animal & Poultry Feed',
    'industry-feed-text': 'Rich calcium source for livestock, poultry, and aquatic feed.',
    'industry-rubber-title': 'Rubber & Foam',
    'industry-rubber-text': 'Enhances physical properties and flowability in rubber compounds.',
    'industry-construction-title': 'Tiles & Construction',
    'industry-construction-text': 'Used in ceramic bodies, dry mortars, tile adhesives, and putties.',
"""

# Replace old en translations for industry
content = re.sub(r"'industry-paint-title': 'Paint & Coatings'.*?'industry-construction-text': 'Essential raw material for cement, mortar, dry-mix, and tile adhesives.',", en_updates.strip() + ',', content, flags=re.DOTALL)


# 2. Update the 'fa' dictionary
fa_updates = """
    'industry-paint-title': 'رنگ و رزین',
    'industry-paint-text': 'پرکننده معدنی پرکاربرد در تولید انواع رنگ و پوشش‌های صنعتی.',
    'industry-plastics-title': 'پلاستیک و پلیمر',
    'industry-plastics-text': 'فیلر با کیفیت برای مستربچ و کامپاندهای پلیمری.',
    'industry-pvc-title': 'PVC، UPVC و پروفیل',
    'industry-pvc-text': 'ماده اساسی در تولید پروفیل در و پنجره، دیوارپوش و کفپوش.',
    'industry-paper-title': 'کاغذ و مقوا',
    'industry-paper-text': 'بهبود سفیدی، یکنواختی سطح و قابلیت چاپ‌پذیری.',
    'industry-feed-title': 'خوراک دام و طیور',
    'industry-feed-text': 'منبع غنی کلسیم برای خوراک دام، طیور و آبزیان.',
    'industry-rubber-title': 'صنایع لاستیک و فوم',
    'industry-rubber-text': 'بهبود خواص فیزیکی و جریان‌پذیری در آمیزه‌های لاستیکی.',
    'industry-construction-title': 'کاشی و سرامیک',
    'industry-construction-text': 'استفاده در بدنه سرامیک، ملات خشک، چسب کاشی و بتونه.',
"""

content = re.sub(r"'industry-paint-title': 'رنگ و پوشش'.*?'industry-construction-text': 'مواد اولیه ضروری برای سیمان، ملات، مخلوط‌های خشک و چسب کاشی.',", fa_updates.strip() + ',', content, flags=re.DOTALL)


# 3. Update elementsToTranslate mapping
elements_updates = """
    'industry-paint-title': '#industry-paint .industry-card__title',
    'industry-paint-text': '#industry-paint .industry-card__text',
    'industry-plastics-title': '#industry-plastics .industry-card__title',
    'industry-plastics-text': '#industry-plastics .industry-card__text',
    'industry-pvc-title': '#industry-pvc .industry-card__title',
    'industry-pvc-text': '#industry-pvc .industry-card__text',
    'industry-paper-title': '#industry-paper .industry-card__title',
    'industry-paper-text': '#industry-paper .industry-card__text',
    'industry-feed-title': '#industry-feed .industry-card__title',
    'industry-feed-text': '#industry-feed .industry-card__text',
    'industry-rubber-title': '#industry-rubber .industry-card__title',
    'industry-rubber-text': '#industry-rubber .industry-card__text',
    'industry-construction-title': '#industry-construction .industry-card__title',
    'industry-construction-text': '#industry-construction .industry-card__text',
"""

content = re.sub(r"'industry-paint-title': '#industry-paint \.industry-card__title'.*?'industry-construction-text': '#industry-construction \.industry-card__text',", elements_updates.strip() + ',', content, flags=re.DOTALL)


# 4. Update the industryData dynamically
fa_industry_data = """
        if (lang === 'fa') {
            industryData.paint.title = 'رنگ و رزین';
            industryData.paint.description = 'پودر میکرونیزه کربنات کلسیم بهعنوان یکی از پرکنندههای معدنی پرکاربرد در تولید انواع رنگ، رزین و پوششهای صنعتی استفاده میشود. این ماده با برخورداری از سفیدی مطلوب و دانهبندی یکنواخت، به بهبود پوششدهی، تنظیم غلظت و ایجاد بافت مناسب در محصول نهایی کمک میکند. استفاده از گرید مناسب کربنات کلسیم میتواند ضمن حفظ کیفیت، باعث بهینهسازی فرمولاسیون و کاهش هزینههای تولید شود. این محصول در تولید رنگهای ساختمانی، رنگهای صنعتی، پرایمرها، بتونهها و انواع پوششهای پایه آب و پایه حلال کاربرد دارد. انتخاب گرید مناسب بر اساس میزان سفیدی، اندازه ذرات، جذب روغن و قابلیت پراکنش در فرمولاسیون انجام میشود.';
            industryData.paint.specs = [];

            industryData.plastics.title = 'پلاستیک و پلیمر';
            industryData.plastics.description = 'پودر میکرونیزه کربنات کلسیم یکی از پرکنندههای معدنی پرمصرف در صنایع پلاستیک و پلیمر است و در تولید طیف گستردهای از محصولات پلیمری به کار میرود. دانهبندی کنترلشده، رطوبت پایین و پراکنشپذیری مناسب این ماده، به یکنواختی ترکیب و پایداری فرآیند تولید کمک میکند. گریدهای معمولی و کوتد کربنات کلسیم، بسته به نوع پلیمر و فرمولاسیون، برای بهبود خواص فرآیندی و تنظیم ویژگیهای محصول نهایی انتخاب میشوند. این محصول در تولید مستربچ، فیلمهای پلیمری، محصولات تزریقی، قطعات پلاستیکی و کامپاندهای پلیمری کاربرد دارد. انتخاب گرید مناسب با توجه به اندازه ذرات، میزان پوششدهی سطحی، سفیدی و الزامات محصول نهایی انجام میشود.';
            industryData.plastics.specs = [];

            industryData.pvc.title = 'PVC، UPVC و پروفیل';
            industryData.pvc.description = 'پودر میکرونیزه کربنات کلسیم یکی از مواد معدنی مهم در فرمولاسیون محصولات PVC و UPVC است و در تولید پروفیلهای در و پنجره، دیوارپوش، قرنیز، کفپوش و قطعات ساختمانی کاربرد گسترده دارد. یکنواختی دانهبندی، سفیدی مناسب و رطوبت پایین پودر در کیفیت ظاهری محصول، پایداری فرآیند اکستروژن و یکنواختی تولید نقش دارد. گریدهای کوتد بهدلیل پراکنش بهتر در ماتریس پلیمری، در بسیاری از فرمولاسیونهای PVC مورد استفاده قرار میگیرند. انتخاب گرید مناسب با توجه به نوع محصول، درصد مصرف، سرعت تولید و ویژگیهای مکانیکی و ظاهری مورد انتظار انجام میشود. کنترل مستمر کیفیت پودر، به تولید پایدار و کاهش نوسان در فرآیند کمک میکند.';
            industryData.pvc.specs = [];

            industryData.paper.title = 'کاغذ و مقوا';
            industryData.paper.description = 'پودر میکرونیزه کربنات کلسیم یکی از پرکنندههای معدنی پرکاربرد در صنعت کاغذ و مقوا است و در تولید انواع کاغذ و مقوای بستهبندی و چاپ استفاده میشود. این ماده میتواند به بهبود سفیدی، یکنواختی سطح و کیفیت ظاهری محصول کمک کند و در نتیجه قابلیت چاپپذیری و جلوه نهایی را ارتقا دهد. کنترل دانهبندی، خلوص و ثبات کیفیت پودر، برای دستیابی به تولید پایدار و محصول یکنواخت اهمیت بالایی دارد. کربنات کلسیم میتواند در کاربردهای فیلر و همچنین برخی فرمولاسیونهای کوتینگ مورد استفاده قرار گیرد. انتخاب گرید مناسب بر اساس نوع خط تولید، مشخصات کاغذ/مقوا و نیازهای فنی مصرفکننده انجام میشود.';
            industryData.paper.specs = [];

            industryData.feed.title = 'خوراک دام، طیور و آبزیان';
            industryData.feed.description = 'پودر میکرونیزه کربنات کلسیم یک منبع غنی از کلسیم برای تأمین نیازهای حیاتی در صنعت خوراک دام، طیور و آبزیان محسوب میشود. این ماده در تقویت استخوانبندی، بهبود کیفیت پوسته تخممرغ در طیور و تنظیم سوختوساز بدن دام نقش کلیدی ایفا میکند. خلوص بالا، عدم وجود ناخالصیهای فلزات سنگین و دانهبندی دقیق، از ویژگیهای حائز اهمیت این پودر برای اطمینان از جذب حداکثری و سلامت محصولات نهایی است. استفاده از گرید مناسب با اندازه ذرات کنترلشده، به توزیع یکنواخت در فرمولاسیون و افزایش راندمان تولید خوراک کمک میکند. این محصول با استانداردهای بهداشتی و تغذیهای سازگاری کامل دارد و در تولید انواع کنسانترهها و مکملهای دامی، طیور و آبزیان به شکل گسترده استفاده میشود.';
            industryData.feed.specs = [];

            industryData.rubber.title = 'صنایع لاستیک و فوم';
            industryData.rubber.description = 'پودر میکرونیزه کربنات کلسیم بهعنوان یک پرکننده معدنی کلیدی در صنایع لاستیک و فوم، نقش مؤثری در بهبود خواص فیزیکی و کاهش هزینههای تولید دارد. استفاده از این ماده در فرمولاسیون محصولات لاستیکی، علاوه بر افزایش سختی و مدول الاستیسیته، به بهبود ویژگیهای پردازشی و جریانپذیری آمیزه در فرآیند تولید کمک میکند. در صنایع تولید انواع فوم، این پودر با حفظ یکنواختی سلولی و ساختار نهایی، کیفیت و دوام محصول را ارتقا میدهد. انتخاب گرید مناسب با دانهبندی دقیق و جذب روغن بهینه، تأثیر مستقیمی بر پایداری ابعادی و مقاومت سایشی محصولات نهایی خواهد داشت.';
            industryData.rubber.specs = [];

            industryData.construction.title = 'کاشی، سرامیک و ساختمان';
            industryData.construction.description = 'پودر میکرونیزه کربنات کلسیم در تولید انواع کاشی، سرامیک و مصالح ساختمانی بهعنوان یک ماده معدنی پرکاربرد استفاده میشود. این محصول در فرمولاسیون بدنههای سرامیکی، ملاتهای خشک، چسب کاشی، بتونه، گچهای پلیمری و پوششهای ساختمانی نقش مؤثری دارد. یکنواختی دانهبندی و کیفیت پایدار پودر، به کنترل بهتر فرآیند تولید و افزایش کیفیت محصول نهایی کمک شایانی میکند. انتخاب گرید مناسب با توجه به ویژگیهای فنی مورد نیاز و شرایط خط تولید، دستیابی به بافت مطلوب و مقاومت فیزیکی مورد انتظار را تضمین مینماید. کربنات کلسیم میکرونیزه با ایجاد خواص پرکنندگی عالی، در بهینهسازی فرمولاسیون محصولات ساختمانی و سرامیکی نقش اساسی ایفا میکند.';
            industryData.construction.specs = [];
        } else {
            // Restore English industry data
            industryData.paint.title = 'Paint & Resin';
            industryData.paint.description = 'Micronized calcium carbonate powder is used as one of the most widely used mineral fillers in the production of various industrial paints, resins, and coatings. Having desirable whiteness and uniform granulation, it helps improve coverage, adjust viscosity, and create appropriate texture in the final product. Using the right grade of calcium carbonate can optimize formulation and reduce production costs while maintaining quality. This product is used in the production of architectural paints, industrial paints, primers, putties, and various water-based and solvent-based coatings. Selecting the right grade is based on whiteness, particle size, oil absorption, and dispersibility in the formulation.';
            industryData.paint.specs = [];

            industryData.plastics.title = 'Plastics & Polymers';
            industryData.plastics.description = 'Micronized calcium carbonate powder is one of the most consumed mineral fillers in the plastics and polymer industries, used in producing a wide range of polymeric products. Its controlled granulation, low moisture, and good dispersibility contribute to blend uniformity and production process stability. Regular and coated calcium carbonate grades are selected based on the polymer type and formulation to improve processing properties and final product characteristics. It is applied in manufacturing masterbatches, polymer films, injection molded products, plastic parts, and polymer compounds. Grade selection considers particle size, surface coating, whiteness, and end-product requirements.';
            industryData.plastics.specs = [];

            industryData.pvc.title = 'PVC, UPVC & Profiles';
            industryData.pvc.description = 'Micronized calcium carbonate powder is an essential mineral in PVC and UPVC product formulations, widely used in manufacturing door and window profiles, wall panels, baseboards, flooring, and construction parts. The powder\\'s granulation uniformity, suitable whiteness, and low moisture impact the product\\'s visual quality, extrusion stability, and production consistency. Coated grades are utilized in many PVC formulations due to better dispersion in the polymer matrix. The appropriate grade is chosen based on product type, usage percentage, production speed, and expected mechanical and visual properties. Continuous powder quality control ensures stable production and reduces process fluctuations.';
            industryData.pvc.specs = [];

            industryData.paper.title = 'Paper & Cardboard';
            industryData.paper.description = 'Micronized calcium carbonate powder is a highly utilized mineral filler in the paper and cardboard industry, used to produce various packaging and printing papers and boards. This material improves the product\\'s whiteness, surface uniformity, and visual quality, thereby enhancing printability and final appearance. Controlling the powder\\'s granulation, purity, and quality stability is crucial for achieving stable production and a uniform product. Calcium carbonate is used in filler applications as well as certain coating formulations. Grade selection depends on the production line type, paper/cardboard specifications, and consumer technical needs.';
            industryData.paper.specs = [];

            industryData.feed.title = 'Animal, Poultry & Aquatic Feed';
            industryData.feed.description = 'Micronized calcium carbonate powder is considered a rich source of calcium for meeting vital needs in the animal, poultry, and aquatic feed industry. This substance plays a key role in strengthening skeletal structure, improving eggshell quality in poultry, and regulating animal metabolism. High purity, the absence of heavy metal impurities, and precise granulation are significant features of this powder to ensure maximum absorption and final product health. Using a suitable grade with controlled particle size helps achieve uniform distribution in the formulation and increases feed production efficiency. This product fully complies with health and nutritional standards and is extensively used in producing various concentrates and supplements for livestock, poultry, and aquatic animals.';
            industryData.feed.specs = [];

            industryData.rubber.title = 'Rubber & Foam';
            industryData.rubber.description = 'Micronized calcium carbonate powder acts as a key mineral filler in the rubber and foam industries, effectively improving physical properties and reducing production costs. Using this material in rubber product formulations not only increases hardness and elastic modulus but also improves processing characteristics and compound flowability during production. In producing various foams, this powder enhances product quality and durability by maintaining uniform cellular structure. Selecting the right grade with precise granulation and optimal oil absorption directly impacts the dimensional stability and abrasion resistance of the final products.';
            industryData.rubber.specs = [];

            industryData.construction.title = 'Tiles, Ceramics & Construction';
            industryData.construction.description = 'Micronized calcium carbonate powder is widely used as an applied mineral in producing various tiles, ceramics, and construction materials. It effectively contributes to the formulations of ceramic bodies, dry mortars, tile adhesives, putties, polymer plasters, and construction coatings. The powder\\'s uniform granulation and stable quality significantly help control the production process and enhance the final product\\'s quality. Choosing the right grade based on required technical features and production line conditions ensures achieving the desired texture and physical resistance. Micronized calcium carbonate plays a fundamental role in optimizing construction and ceramic product formulations by providing excellent filling properties.';
            industryData.construction.specs = [];
        }
"""
content = re.sub(r"        if \(lang === 'fa'\) \{.*?\} else \{\n            // Restore English industry data.*?\n        \}", fa_industry_data, content, flags=re.DOTALL)


with open('lang.js', 'w') as f:
    f.write(content)

