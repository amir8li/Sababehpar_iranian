import re

en_texts = [
    "<strong>1. Energy Optimization and Management:</strong> Due to its energy-intensive nature, the crushing and micronization process at Saba Behpar is carefully managed. By investing in modern equipment and high-efficiency electric motors, we strive to reduce energy consumption in our production unit. Furthermore, our production schedule is designed to distribute workloads intelligently across different hours, preventing excessive strain on the power grid and prioritizing optimal consumption. Our goal is the gradual but continuous reduction of the company's carbon footprint through the smart automation of production line equipment.",
    
    "<strong>2. Waste Management and Zero-Waste Production:</strong> Our approach at Saba Behpar is the maximum utilization of extracted minerals. By adopting a \"three-tier quality grade production\" strategy, we categorize and process all parts of the incoming ore based on their physical and chemical specifications. This precise quality segregation allows us to prevent mineral waste and, instead of discarding, transform every part of the ore into a practical product for various industries. This cycle not only increases economic efficiency but also demonstrates our commitment to the responsible use of natural resources.",
    
    "<strong>3. Advanced Filtration Systems and Air Quality Control:</strong> The health of the working environment air and the area surrounding the factory is a vital priority for us. Saba Behpar's production lines are equipped with the most advanced Bag Filter systems, capable of absorbing 99.9% of suspended particles. Through continuous monitoring, these systems prevent dust from escaping into the open air. This measure not only guarantees clean air for local communities but also provides a healthy, respiratory-pollution-free environment for the factory personnel.",
    
    "<strong>4. Economic Development and Local Workforce Empowerment:</strong> The development of Saba Behpar is intertwined with the development of the Aligoodarz region. Our primary policy is to prioritize the recruitment and employment of local experts and workforce. We believe that human capital is our most valuable asset; therefore, we implement continuous training programs to upgrade the technical knowledge and specialized skills of our local personnel. Our goal is to create sustainable employment where our regional experts act as the main pillars of production at the highest national standards.",
    
    "<strong>5. Occupational Health and Safety Standards (HSE):</strong> At Saba Behpar, safety goes beyond a legal requirement; it is a part of our organizational culture. We have developed and implemented strict protocols for the physical health and safety of all employees. In addition to equipping personnel with advanced personal protective equipment, environmental safety and ventilation systems are designed to neutralize all potential hazards at their inception. Our approach to occupational health is preventive, ensuring that every person who enters the factory in the morning returns home in perfect health at the end of their shift."
]

fa_texts = [
    "<strong>۱. بهینه‌سازی و مدیریت مصرف انرژی:</strong> در شرکت صبا بهپر، فرآیند خردایش و میکرونیزاسیون با توجه به ماهیت انرژی‌بر آن، به دقت مدیریت می‌شود. ما با سرمایه‌گذاری بر تجهیزات مدرن و الکتروموتورهای با بازدهی بالا، سعی در کاهش مصرف انرژی در واحد تولید داریم. همچنین، برنامه تولید ما به‌گونه‌ای تنظیم شده است که با توزیع هوشمندِ بارهای کاری در ساعات مختلف، از فشار مضاعف بر شبکه برق جلوگیری کرده و مصرف بهینه را در اولویت قرار دهیم. هدف ما کاهش تدریجی اما مستمر ردپای کربنی مجموعه از طریق هوشمندسازی تجهیزاتِ خط تولید است.",
    
    "<strong>۲. مدیریت پسماند و تولید بدون ضایعات:</strong> رویکرد ما در صبا بهپر، بهره‌برداری حداکثری از سنگ معدنی استخراج‌شده است. ما با اتخاذ استراتژیِ «تولید در سه گرید کیفیتی»، تمامیِ بخش‌های سنگ ورودی را بر اساس مشخصات فیزیکی و شیمیایی دسته‌بندی و فرآوری می‌کنیم. این تفکیک دقیقِ کیفی، به ما این امکان را می‌دهد که از اتلاف مواد معدنی جلوگیری کرده و به جای دورریز، هر بخش از سنگ را به محصولی کاربردی برای صنایع مختلف تبدیل کنیم. این چرخه، علاوه بر افزایش بهره‌وری اقتصادی، نشان‌دهنده تعهد ما به استفاده مسئولانه از منابع طبیعی است.",
    
    "<strong>۳. سیستم‌های پیشرفته فیلتراسیون و کنترل کیفیت هوا:</strong> سلامت هوای محیط کار و منطقه پیرامون کارخانه برای ما یک اولویت حیاتی است. خطوط تولید صبا بهپر به پیشرفته‌ترین سیستم‌های فیلتراسیون کیسه‌ای (Bag Filters) مجهز شده‌اند که توانایی جذب ۹۹.۹ درصد ذرات معلق را داراست. این تجهیزات با مانیتورینگ مداوم، از نشت غبار به فضای آزاد جلوگیری می‌کنند. این اقدام نه تنها تضمین‌کننده هوایی پاک برای جوامع محلی است، بلکه محیطی سالم و عاری از آلودگی‌های تنفسی را برای پرسنل کارخانه فراهم می‌آورد.",
    
    "<strong>۴. توسعه اقتصادی و توانمندسازی نیروی کار بومی:</strong> توسعه صبا بهپر با توسعه منطقه الیگودرز پیوند خورده است. سیاست اصلی ما، اولویت در استخدام و به‌کارگیری نیروهای متخصص و بومیِ منطقه است. ما معتقدیم که سرمایه انسانی، ارزشمندترین دارایی ماست؛ به همین دلیل، برنامه‌های آموزشی مستمر برای ارتقای دانش فنی و مهارت‌های تخصصیِ پرسنل بومی اجرا می‌کنیم. هدف ما ایجاد اشتغالی پایدار است که در آن، کارشناسان منطقه ما، بازوهای اصلیِ تولید در بالاترین سطح استانداردهای ملی باشند.",
    
    "<strong>۵. استانداردهای ایمنی و سلامت شغلی (HSE):</strong> ایمنی در صبا بهپر فراتر از یک الزام قانونی، بخشی از فرهنگ سازمانی ماست. ما پروتکل‌های سختگیرانه‌ای برای سلامت فیزیکی و ایمنی تمامی کارکنان تدوین و اجرا کرده‌ایم. علاوه بر تجهیز پرسنل به وسایل حفاظت فردی پیشرفته، سیستم‌های تهویه و ایمنی محیطی به‌گونه‌ای طراحی شده‌اند که تمامی خطرات بالقوه را در نطفه خنثی کنند. نگاه ما به سلامت شغلی، نگاهی پیشگیرانه است تا اطمینان حاصل کنیم هر فردی که صبح وارد کارخانه می‌شود، در پایان شیفت کاری با سلامت کامل به خانه بازمی‌گردد."
]

ar_texts = [
    "<strong>١. تحسين وإدارة استهلاك الطاقة:</strong> نظرًا لطبيعتها الكثيفة الاستهلاك للطاقة، تتم إدارة عملية التكسير والميكرونة في صبا بهپر بعناية. من خلال الاستثمار في المعدات الحديثة والمحركات الكهربائية عالية الكفاءة، نسعى جاهدين لتقليل استهلاك الطاقة. كما تم تصميم جدول الإنتاج لتوزيع أعباء العمل بذكاء، مما يمنع الضغط المفرط على شبكة الكهرباء. هدفنا هو التخفيض التدريجي والمستمر للبصمة الكربونية من خلال الأتمتة الذكية.",
    "<strong>٢. إدارة النفايات والإنتاج الخالي من النفايات:</strong> نهجنا هو الاستفادة القصوى من المعادن المستخرجة. من خلال اعتماد استراتيجية \"الإنتاج بثلاث درجات جودة\"، نقوم بتصنيف ومعالجة جميع أجزاء الخام الوارد بناءً على مواصفاتها. يتيح لنا هذا الفصل الدقيق منع هدر المعادن وتحويل كل جزء من الخام إلى منتج عملي، مما يوضح التزامنا بالاستخدام المسؤول للموارد الطبيعية.",
    "<strong>٣. أنظمة الفلترة المتقدمة ومراقبة جودة الهواء:</strong> تعتبر صحة هواء بيئة العمل والمنطقة المحيطة بالمصنع أولوية حيوية. خطوط الإنتاج لدينا مجهزة بأحدث أنظمة الفلاتر الكيسية، القادرة على امتصاص ٩٩.٩٪ من الجسيمات العالقة. من خلال المراقبة المستمرة، تمنع هذه الأنظمة تسرب الغبار إلى الهواء الطلق، مما يضمن هواءً نقيًا للمجتمعات المحلية وبيئة صحية للموظفين.",
    "<strong>٤. التنمية الاقتصادية وتمكين القوى العاملة المحلية:</strong> ترتبط تنمية صبا بهپر بتنمية منطقة أليغودرز. سياستنا الأساسية هي إعطاء الأولوية لتوظيف الخبراء والقوى العاملة المحلية. نحن نؤمن بأن رأس المال البشري هو أثمن أصولنا؛ لذلك، ننفذ برامج تدريبية مستمرة لترقية المعرفة الفنية والمهارات المتخصصة لموظفينا المحليين، بهدف خلق فرص عمل مستدامة.",
    "<strong>٥. معايير الصحة والسلامة المهنية (HSE):</strong> في صبا بهپر، السلامة تتجاوز المتطلبات القانونية؛ إنها جزء من ثقافتنا التنظيمية. لقد قمنا بتطوير وتنفيذ بروتوكولات صارمة للصحة البدنية وسلامة جميع الموظفين. بالإضافة إلى تزويد الموظفين بمعدات الحماية الشخصية المتقدمة، تم تصميم أنظمة السلامة والتهوية البيئية لتحييد جميع المخاطر المحتملة. نهجنا وقائي لضمان عودة كل من يدخل المصنع إلى منزله بصحة تامة."
]

def update_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for i in range(5):
        # find the p tag
        pattern = r'(<p id="about-sust-p' + str(i+1) + r'"[^>]*>).*?(</p>)'
        content = re.sub(pattern, r'\g<1>\n                        ' + en_texts[i] + r'\n                    \2', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_html('about/index.html')
update_html('about/sustainability.html')

with open('lang.js', 'r', encoding='utf-8') as f:
    lang = f.read()

# Update english
for i in range(5):
    lang = re.sub(r"'about-sust-p" + str(i+1) + r"': '[^']+',", f"'about-sust-p{i+1}': '{en_texts[i].replace(chr(39), chr(92) + chr(39))}',", lang)

# Update farsi
# we need to be careful not to replace english ones again.
# wait, my regex replaced ALL occurrences of about-sust-pX.
# it's better to just read lang.js and do specific replaces
