import streamlit as st
import qrcode
from PIL import Image
import io
import base64
import os

# 设置页面配置
st.set_page_config(
    page_title="企业数据系统平台",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义CSS样式
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# 内联CSS样式
def inline_css():
    st.markdown("""
    <style>
        :root {
            --primary: #165DFF;
            --secondary: #722ED1;
            --accent: #00B42A;
            --neutral: #F5F7FA;
            --dark: #1D2939;
        }
        
        .stApp {
            background-color: #F9FAFB;
            font-family: 'Inter', 'system-ui', 'sans-serif';
        }
        
        /* 导航栏样式 */
        .navbar {
            position: sticky;
            top: 0;
            z-index: 50;
            background-color: white;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            padding: 1rem 0;
            transition: all 0.3s ease;
        }
        
        .navbar-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .logo i {
            color: var(--primary);
            font-size: 1.5rem;
        }
        
        .logo h1 {
            font-size: 1.25rem;
            font-weight: bold;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        
        .nav-links {
            display: flex;
            gap: 1.5rem;
        }
        
        .nav-links a {
            color: #1F2937;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        .nav-links a:hover {
            color: var(--primary);
        }
        
        /* 英雄区域样式 */
        .hero {
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
            padding: 4rem 0;
            position: relative;
            text-align: center;
        }
        
        .hero-content {
            max-width: 48rem;
            margin: 0 auto;
            padding: 0 1rem;
        }
        
        .hero h1 {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1.5rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .hero p {
            font-size: 1.125rem;
            color: #F3F4F6;
            margin-bottom: 2.5rem;
        }
        
        .hero-button {
            display: inline-block;
            background-color: white;
            color: var(--primary);
            font-weight: 600;
            padding: 0.75rem 2rem;
            border-radius: 9999px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
            text-decoration: none;
        }
        
        .hero-button:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
        
        /* 系统卡片样式 */
        .section {
            padding: 4rem 0;
        }
        
        .section-header {
            text-align: center;
            margin-bottom: 4rem;
        }
        
        .section-header h2 {
            font-size: 2rem;
            font-weight: bold;
            color: var(--dark);
            margin-bottom: 1rem;
        }
        
        .section-header p {
            color: #374151;
            max-width: 48rem;
            margin: 0 auto;
        }
        
        .card-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }
        
        .card {
            background-color: white;
            border-radius: 0.75rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            overflow: hidden;
            transition: all 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-10px);
        }
        
        .card-image {
            height: 12rem;
            overflow: hidden;
        }
        
        .card-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }
        
        .card:hover .card-image img {
            transform: scale(1.1);
        }
        
        .card-content {
            padding: 1.5rem;
        }
        
        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }
        
        .card-icon {
            width: 2.5rem;
            height: 2.5rem;
            border-radius: 9999px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 0.75rem;
        }
        
        .card-icon.blue {
            background-color: rgba(22, 93, 255, 0.1);
        }
        
        .card-icon.purple {
            background-color: rgba(114, 46, 209, 0.1);
        }
        
        .card-icon.green {
            background-color: rgba(0, 180, 42, 0.1);
        }
        
        .card-icon i {
            font-size: 1.25rem;
        }
        
        .card-icon.blue i {
            color: var(--primary);
        }
        
        .card-icon.purple i {
            color: var(--secondary);
        }
        
        .card-icon.green i {
            color: var(--accent);
        }
        
        .card-title {
            font-size: 1.25rem;
            font-weight: bold;
            color: #000000;
        }
        
        .card-description {
            color: #374151;
            margin-bottom: 1.5rem;
        }
        
        .card-button {
            display: inline-block;
            width: 100%;
            text-align: center;
            padding: 0.75rem;
            border-radius: 0.5rem;
            font-weight: 500;
            color: white;
            text-decoration: none;
            transition: background-color 0.3s ease;
        }
        
        .card-button.blue {
            background-color: var(--primary);
        }
        
        .card-button.blue:hover {
            background-color: rgba(22, 93, 255, 0.9);
        }
        
        .card-button.purple {
            background-color: var(--secondary);
        }
        
        .card-button.purple:hover {
            background-color: rgba(114, 46, 209, 0.9);
        }
        
        .card-button.green {
            background-color: var(--accent);
        }
        
        .card-button.green:hover {
            background-color: rgba(0, 180, 42, 0.9);
        }
        
        /* 特性网格样式 */
        .features {
            background-color: var(--neutral);
            padding: 4rem 0;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }
        
        .feature-card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 0.75rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        
        .feature-icon {
            width: 3rem;
            height: 3rem;
            border-radius: 9999px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1rem;
        }
        
        .feature-icon.blue {
            background-color: rgba(22, 93, 255, 0.1);
        }
        
        .feature-icon.purple {
            background-color: rgba(114, 46, 209, 0.1);
        }
        
        .feature-icon.green {
            background-color: rgba(0, 180, 42, 0.1);
        }
        
        .feature-icon.yellow {
            background-color: rgba(245, 158, 11, 0.1);
        }
        
        .feature-icon i {
            font-size: 1.25rem;
        }
        
        .feature-icon.blue i {
            color: var(--primary);
        }
        
        .feature-icon.purple i {
            color: var(--secondary);
        }
        
        .feature-icon.green i {
            color: var(--accent);
        }
        
        .feature-icon.yellow i {
            color: #F59E0B;
        }
        
        .feature-title {
            font-size: 1.125rem;
            font-weight: 600;
            color: #000000;
            margin-bottom: 0.5rem;
        }
        
        .feature-description {
            color: #374151;
            font-size: 0.875rem;
        }
        
        /* 二维码区域样式 */
        .qrcode-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            max-width: 48rem;
            margin: 0 auto;
            padding: 0 1rem;
        }
        
        .qrcode-item {
            text-align: center;
        }
        
        .qrcode-image {
            background-color: white;
            padding: 1rem;
            border-radius: 0.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            display: inline-block;
            margin-bottom: 1rem;
        }
        
        .qrcode-title {
            font-weight: 600;
            color: #000000;
            margin-bottom: 0.25rem;
        }
        
        .qrcode-subtitle {
            color: #4B5563;
            font-size: 0.875rem;
        }
        
        /* 关于我们样式 */
        .about {
            background-color: var(--dark);
            color: white;
            padding: 4rem 0;
            text-align: center;
        }
        
        .about-content {
            max-width: 48rem;
            margin: 0 auto;
            padding: 0 1rem;
        }
        
        .about h2 {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 1.5rem;
        }
        
        .about p {
            color: #E5E7EB;
            margin-bottom: 2rem;
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
        }
        
        .social-links a {
            color: white;
            font-size: 1.25rem;
            transition: color 0.3s ease;
        }
        
        .social-links a:hover {
            color: var(--primary);
        }
        
        /* 页脚样式 */
        .footer {
            background-color: #1F2937;
            color: white;
            padding: 2rem 0;
            text-align: center;
        }
        
        .footer-content {
            font-size: 0.875rem;
            color: #D1D5DB;
        }
        
        .footer p {
            margin-bottom: 0.5rem;
        }
        
        /* 返回顶部按钮 */
        .back-to-top {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background-color: var(--primary);
            color: white;
            width: 3rem;
            height: 3rem;
            border-radius: 9999px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            cursor: pointer;
            z-index: 40;
        }
        
        .back-to-top.visible {
            opacity: 1;
            visibility: visible;
        }
        
        /* 响应式调整 */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }
            
            .hero h1 {
                font-size: 1.875rem;
            }
            
            .hero p {
                font-size: 1rem;
            }
            
            .section-header h2 {
                font-size: 1.5rem;
            }
            
            .about h2 {
                font-size: 1.5rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

# 生成二维码
def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 转换为base64以便在HTML中显示
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

# 主函数
def main():
    # 应用内联CSS
    inline_css()
    
    # 导航栏
    st.markdown("""
    <div class="navbar">
        <div class="navbar-content">
            <div class="logo">
                <i class="fa fa-line-chart"></i>
                <h1>企业数据系统平台</h1>
            </div>
            <div class="nav-links">
                <a href="#home">首页</a>
                <a href="#systems">系统功能</a>
                <a href="#qrcode">移动端访问</a>
                <a href="#about">关于我们</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 英雄区域
    st.markdown("""
    <section id="home" class="hero">
        <div class="hero-content">
            <h1>企业数据智能分析平台</h1>
            <p>整合企业数字化转型、ESG分析与数据可视化，助力企业决策智能化</p>
            <a href="#systems" class="hero-button">探索系统功能 <i class="fa fa-arrow-right ml-2"></i></a>
        </div>
        <div style="position: absolute; bottom: 0; left: 0; right: 0; height: 4rem; background: linear-gradient(to top, #F9FAFB, transparent);"></div>
    </section>
    """, unsafe_allow_html=True)
    
    # 系统功能介绍
    st.markdown("""
    <section id="systems" class="section">
        <div class="section-header">
            <h2>系统功能介绍</h2>
            <p>我们提供三个专业数据系统，满足企业不同维度的数据分析需求</p>
        </div>
    </section>
    """, unsafe_allow_html=True)
    
    # 系统卡片
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-image">
                <img src="https://picsum.photos/id/180/800/500" alt="企业数字化转型分析系统">
            </div>
            <div class="card-content">
                <div class="card-header">
                    <div class="card-icon blue">
                        <i class="fa fa-cogs"></i>
                    </div>
                    <h3 class="card-title">企业数字化转型分析系统</h3>
                </div>
                <p class="card-description">全面分析企业数字化转型进程，评估各技术应用程度，提供趋势分析与行业对比，助力企业数字化战略决策。</p>
                <a href="https://19992023digital.streamlit.app/" target="_blank" class="card-button blue">
                    进入系统 <i class="fa fa-external-link ml-1"></i>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-image">
                <img src="https://picsum.photos/id/201/800/500" alt="ESG量化数据分析系统">
            </div>
            <div class="card-content">
                <div class="card-header">
                    <div class="card-icon purple">
                        <i class="fa fa-leaf"></i>
                    </div>
                    <h3 class="card-title">ESG量化数据分析系统</h3>
                </div>
                <p class="card-description">专注于企业环境、社会和治理表现的量化分析，提供多维度ESG评估与趋势追踪，支持PDF报告导出。</p>
                <a href="https://esgdigital.streamlit.app/" target="_blank" class="card-button purple">
                    进入系统 <i class="fa fa-external-link ml-1"></i>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-image">
                <img src="https://picsum.photos/id/160/800/500" alt="企业数据可视化平台">
            </div>
            <div class="card-content">
                <div class="card-header">
                    <div class="card-icon green">
                        <i class="fa fa-bar-chart"></i>
                    </div>
                    <h3 class="card-title">企业数据可视化平台</h3>
                </div>
                <p class="card-description">整合企业多维度数据，通过交互式图表直观展示企业表现，支持自定义筛选与深度数据分析。</p>
                <a href="https://20072023digital.streamlit.app/" target="_blank" class="card-button green">
                    进入系统 <i class="fa fa-external-link ml-1"></i>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # 功能特点
    st.markdown("""
    <section class="features">
        <div class="section-header">
            <h2>平台核心优势</h2>
            <p>我们的系统整合多项先进技术，为企业提供全方位数据分析解决方案</p>
        </div>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon blue">
                    <i class="fa fa-database"></i>
                </div>
                <h3 class="feature-title">全面数据整合</h3>
                <p class="feature-description">整合企业多维度数据，提供全方位分析视角</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon purple">
                    <i class="fa fa-line-chart"></i>
                </div>
                <h3 class="feature-title">深度数据分析</h3>
                <p class="feature-description">专业算法模型，挖掘数据背后的商业价值</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon green">
                    <i class="fa fa-mobile"></i>
                </div>
                <h3 class="feature-title">全平台支持</h3>
                <p class="feature-description">响应式设计，完美支持电脑与移动设备访问</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon yellow">
                    <i class="fa fa-file-pdf-o"></i>
                </div>
                <h3 class="feature-title">报告导出</h3>
                <p class="feature-description">一键生成专业PDF报告，支持数据分享与汇报</p>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)
    
    # 二维码区域
    st.markdown("""
    <section id="qrcode" class="section">
        <div class="section-header">
            <h2>移动端访问</h2>
            <p>扫描下方二维码，在手机上访问我们的系统</p>
        </div>
    </section>
    """, unsafe_allow_html=True)
    
    # 生成二维码
    qr1 = generate_qr_code("https://19992023digital.streamlit.app/")
    qr2 = generate_qr_code("https://20072023digital.streamlit.app/")
    qr3 = generate_qr_code("https://esgdigital.streamlit.app/")
    
    # 显示二维码
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="qrcode-item">
            <div class="qrcode-image">
                <img src="{qr1}" alt="企业数字化转型分析系统二维码" style="width: 192px; height: 192px;">
            </div>
            <h3 class="qrcode-title">数字化转型系统</h3>
            <p class="qrcode-subtitle">扫码访问移动端</p>
            <p style="color: #374151; font-size: 0.875rem; margin-top: 0.5rem;">https://19992023digital.streamlit.app/</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="qrcode-item">
            <div class="qrcode-image">
                <img src="{qr2}" alt="ESG量化数据分析系统二维码" style="width: 192px; height: 192px;">
            </div>
            <h3 class="qrcode-title">ESG分析系统</h3>
            <p class="qrcode-subtitle">扫码访问移动端</p>
            <p style="color: #374151; font-size: 0.875rem; margin-top: 0.5rem;">https://20072023digital.streamlit.app/</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="qrcode-item">
            <div class="qrcode-image">
                <img src="{qr3}" alt="企业数据可视化平台二维码" style="width: 192px; height: 192px;">
            </div>
            <h3 class="qrcode-title">数据可视化平台</h3>
            <p class="qrcode-subtitle">扫码访问移动端</p>
            <p style="color: #374151; font-size: 0.875rem; margin-top: 0.5rem;">https://esgdigital.streamlit.app/</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 关于我们
    st.markdown("""
    <section id="about" class="about">
        <div class="about-content">
            <h2>关于我们</h2>
            <p>我们致力于为企业提供专业的数据洞察与分析工具，助力企业数字化转型与可持续发展。通过先进的数据分析技术，帮助企业发现潜在价值，优化决策流程。</p>
            <div class="social-links">
                <a href="#"><i class="fa fa-envelope"></i></a>
                <a href="#"><i class="fa fa-github"></i></a>
                <a href="#"><i class="fa fa-linkedin"></i></a>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)
    
    # 页脚
    st.markdown("""
    <footer class="footer">
        <div class="footer-content">
            <p>&copy; 2025 企业数据系统平台 版权所有</p>
            <p>本系统仅供学习和研究使用</p>
        </div>
    </footer>
    """, unsafe_allow_html=True)
    
    # 返回顶部按钮
    st.markdown("""
    <div id="back-to-top" class="back-to-top">
        <i class="fa fa-arrow-up"></i>
    </div>
    
    <script>
    // 返回顶部按钮功能
    const backToTopButton = document.getElementById('back-to-top');
    
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTopButton.classList.add('visible');
        } else {
            backToTopButton.classList.remove('visible');
        }
    });
    
    backToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // 平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    </script>
    """, unsafe_allow_html=True)

# 加载Font Awesome图标
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
""", unsafe_allow_html=True)

# 运行主函数
if __name__ == "__main__":
    main()

