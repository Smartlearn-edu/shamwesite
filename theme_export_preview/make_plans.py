import re

with open('plans.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_index = 0
end_index = 0

for i, line in enumerate(lines):
    if '<!-- 2. HERO WELCOME SECTION' in line:
        start_index = i
    if '<!-- 13. PARENTS COMMUNITY' in line:
        end_index = i

header_lines = lines[:start_index]
footer_lines = lines[end_index:]

plans_html = """
    <!-- HERO SECTION -->
    <section class="py-20 bg-slate-900/40 relative z-10 border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6">
            <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20 text-sm font-semibold">
                <i class="fas fa-star text-amber-400"></i>
                مركز الشام للثقافة والتعليم
            </span>
            <h2 class="text-4xl md:text-5xl font-extrabold leading-tight tracking-wide text-white">
                بناء الأجيال.. على قيم العلم والقرآن
            </h2>
            <p class="text-lg md:text-xl text-slate-300 leading-relaxed max-w-3xl mx-auto">
                يسر مركز الشام للثقافة والتعليم أن يقدم لكم باقاته التعليمية المعتمدة لتعليم اللغة العربية، القرآن الكريم، والوعي التربوي والتنموي، والمصممة لتلبي احتياجات أبنائكم بمرونة تامة.
            </p>
        </div>
    </section>

    <!-- PLANS SECTION -->
    <section class="py-20 relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-16 space-y-3">
            <h2 class="text-3xl md:text-4xl font-extrabold text-white">
                الباقات التعليمية الثلاث
            </h2>
            <p class="text-slate-400 text-base md:text-lg">
                خياراتنا التعليمية المتميزة.. مرونة وثقة وبناء حقيقي
            </p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
            
            <!-- PLAN 1 -->
            <div class="glass-panel p-8 rounded-3xl border border-teal-500/20 hover:border-teal-500 transition-all flex flex-col justify-between bg-slate-900/60 relative overflow-hidden group">
                <div class="absolute top-0 right-0 w-32 h-32 bg-teal-500/10 rounded-full blur-3xl pointer-events-none group-hover:bg-teal-500/20 transition-all"></div>
                <div class="space-y-6 relative z-10">
                    <div class="w-16 h-16 rounded-2xl bg-teal-500/10 text-teal-400 flex items-center justify-center mb-6">
                        <i class="fas fa-box-open text-3xl"></i>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-white mb-2">1. باقة (التعليم المنهجي)</h3>
                        <p class="text-teal-400 text-sm font-semibold">التأسيس المعتمد المتكامل</p>
                    </div>
                    
                    <div class="py-4 border-y border-slate-800/80">
                        <div class="flex items-baseline gap-2">
                            <span class="text-4xl font-extrabold text-white">25</span>
                            <span class="text-slate-400">يورو / شهرياً</span>
                        </div>
                    </div>

                    <ul class="space-y-4 text-sm text-slate-300">
                        <li class="flex items-start gap-3">
                            <i class="fas fa-calendar-alt text-teal-400 mt-1"></i>
                            <span>3 دروس أسبوعياً.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fas fa-clock text-teal-400 mt-1"></i>
                            <span>مدة الدرس: 45 دقيقة للتمهيدي / ساعة كاملة للمراحل الستة المتقدمة.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fas fa-book-open text-teal-400 mt-1"></i>
                            <span>(قاعدة نورانية - لغة عربية - قرآن كريم).</span>
                        </li>
                    </ul>
                </div>
                
                <div class="pt-8 mt-auto relative z-10">
                    <a href="https://wa.me/YOUR_NUMBER" class="w-full py-4 bg-teal-600 hover:bg-teal-500 text-white font-extrabold rounded-xl flex items-center justify-center gap-2 transition-all shadow-lg shadow-teal-500/20">
                        <i class="fab fa-whatsapp text-xl"></i>
                        <span>تواصل للحجز</span>
                    </a>
                </div>
            </div>

            <!-- PLAN 2 -->
            <div class="glass-panel p-8 rounded-3xl border border-amber-500/40 hover:border-amber-500 transition-all flex flex-col justify-between bg-slate-900/60 relative overflow-hidden group transform md:-translate-y-4 shadow-2xl shadow-amber-500/10">
                <div class="absolute top-0 right-0 w-32 h-32 bg-amber-500/10 rounded-full blur-3xl pointer-events-none group-hover:bg-amber-500/20 transition-all"></div>
                <div class="absolute top-4 left-4">
                    <span class="bg-amber-500/20 text-amber-400 border border-amber-500/30 text-xs px-3 py-1 rounded-full font-bold">الأكثر مرونة</span>
                </div>
                
                <div class="space-y-6 relative z-10">
                    <div class="w-16 h-16 rounded-2xl bg-amber-500/10 text-amber-400 flex items-center justify-center mb-6">
                        <i class="fas fa-user-friends text-3xl"></i>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-white mb-2">2. باقة (التعليم المنهجي الخاص)</h3>
                        <p class="text-amber-400 text-sm font-semibold">خصوصية تامة ومجموعات صغيرة مخصصة</p>
                    </div>
                    
                    <div class="py-4 border-y border-slate-800/80">
                        <div class="flex items-baseline gap-2">
                            <span class="text-slate-400 text-sm">تبدأ من</span>
                            <span class="text-4xl font-extrabold text-white">8</span>
                            <span class="text-slate-400">يورو / للدرس</span>
                        </div>
                    </div>

                    <ul class="space-y-4 text-sm text-slate-300">
                        <li class="flex items-start gap-3">
                            <i class="fas fa-clock text-amber-400 mt-1"></i>
                            <span>مدة الدرس: نصف ساعة (3 دروس في الأسبوع).</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fas fa-check-circle text-amber-400 mt-1"></i>
                            <span>نفس الترتيب والمنهج التعليمي للمركز.</span>
                        </li>
                        <li class="flex items-start gap-3 flex-col w-full">
                            <div class="flex gap-2">
                                <i class="fas fa-coins text-amber-400 mt-1"></i>
                                <span class="font-bold">تكلفة الدرس الواحد (للمجموعة بحد أقصى 4 أطفال):</span>
                            </div>
                            <div class="bg-slate-950/50 rounded-xl p-3 w-full border border-slate-800/80 space-y-2 mt-2">
                                <div class="flex justify-between text-xs"><span class="text-slate-400">طفل واحد منفرد</span><span class="font-bold text-amber-400">8€</span></div>
                                <div class="flex justify-between text-xs"><span class="text-slate-400">طفلين</span><span class="font-bold text-amber-400">10€</span></div>
                                <div class="flex justify-between text-xs"><span class="text-slate-400">3 أطفال</span><span class="font-bold text-amber-400">12€</span></div>
                                <div class="flex justify-between text-xs"><span class="text-slate-400">4 أطفال</span><span class="font-bold text-amber-400">14€</span></div>
                                <p class="text-[10px] text-slate-500 mt-2 border-t border-slate-800 pt-2 text-center">(تكلفة ثابتة للمجموعة، تزيد بمقدار 2 يورو لكل طفل ينضم حديثاً)</p>
                            </div>
                        </li>
                    </ul>
                </div>
                
                <div class="pt-8 mt-auto relative z-10">
                    <a href="https://wa.me/YOUR_NUMBER" class="w-full py-4 bg-amber-500 hover:bg-amber-400 text-slate-900 font-extrabold rounded-xl flex items-center justify-center gap-2 transition-all shadow-lg shadow-amber-500/20">
                        <i class="fab fa-whatsapp text-xl"></i>
                        <span>تواصل للحجز</span>
                    </a>
                </div>
            </div>

            <!-- PLAN 3 -->
            <div class="glass-panel p-8 rounded-3xl border border-indigo-500/20 hover:border-indigo-500 transition-all flex flex-col justify-between bg-slate-900/60 relative overflow-hidden group">
                <div class="absolute top-0 right-0 w-32 h-32 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none group-hover:bg-indigo-500/20 transition-all"></div>
                <div class="space-y-6 relative z-10">
                    <div class="w-16 h-16 rounded-2xl bg-indigo-500/10 text-indigo-400 flex items-center justify-center mb-6">
                        <i class="fas fa-door-open text-3xl"></i>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-white mb-2">3. باقة (التعليم المفتوح الخاص)</h3>
                        <p class="text-indigo-400 text-sm font-semibold">برنامج دراسي ومواعيد من تصميمكم بالكامل</p>
                    </div>
                    
                    <div class="py-4 border-y border-slate-800/80">
                        <div class="flex items-baseline gap-2">
                            <span class="text-2xl font-extrabold text-white">تكلفة مخصصة</span>
                        </div>
                        <p class="text-xs text-slate-400 mt-1">حسب الخطة المطلوبة</p>
                    </div>

                    <ul class="space-y-4 text-sm text-slate-300">
                        <li class="flex items-start gap-3">
                            <i class="fas fa-sliders-h text-indigo-400 mt-1"></i>
                            <span>الدرس ساعة كاملة (تحديد عدد الدروس والمواعيد بحرية تامة).</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fas fa-users-cog text-indigo-400 mt-1"></i>
                            <span>مجموعات خاصة حسب رغبتكم (بشرط ألا يتجاوز العدد 8 أطفال).</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fas fa-layer-group text-indigo-400 mt-1"></i>
                            <span>تحديد المواد حسب رغبة الأهل: (لغة عربية | قرآن كريم | ثقافة عامة: إسلامية، تربوية، وتنموية).</span>
                        </li>
                    </ul>
                </div>
                
                <div class="pt-8 mt-auto relative z-10">
                    <a href="https://wa.me/YOUR_NUMBER" class="w-full py-4 bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold rounded-xl flex items-center justify-center gap-2 transition-all shadow-lg shadow-indigo-500/20">
                        <i class="fab fa-whatsapp text-xl"></i>
                        <span>تواصل للحجز</span>
                    </a>
                </div>
            </div>

        </div>
    </section>

"""

new_lines = header_lines + [plans_html] + footer_lines

with open('plans.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
