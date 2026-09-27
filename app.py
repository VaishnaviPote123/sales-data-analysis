import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Sales Data Analysis",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_csv("data/samplesuperstore.csv")

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    return df


df = load_data()


# ============================================================
# SESSION STATE FOR NAVIGATION
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = 0


pages = [
    "Home",
    "Sales Overview",
    "Category Analysis",
    "Regional Analysis",
    "Product Analysis",
    "Monthly Trends",
    "Customer & Shipping",
    "Correlation Analysis"
]


# ============================================================
# NAVIGATION FUNCTIONS
# ============================================================

def next_page():
    if st.session_state.page < len(pages) - 1:
        st.session_state.page += 1


def previous_page():
    if st.session_state.page > 0:
        st.session_state.page -= 1


def home_page():
    st.session_state.page = 0


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📊 Sales Dashboard")

selected_page = st.sidebar.selectbox(
    "Go to View",
    pages,
    index=st.session_state.page
)

st.session_state.page = pages.index(selected_page)

st.sidebar.markdown("---")

st.sidebar.write("### Dataset Information")
st.sidebar.write(f"Records: **{len(df):,}**")
st.sidebar.write(f"Columns: **{len(df.columns)}**")

st.sidebar.markdown("---")
st.sidebar.write("### Navigation")
st.sidebar.write("Use the buttons below to move between views.")


# ============================================================
# COMMON METRICS
# ============================================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
average_sales = df["Sales"].mean()

profit_margin = (total_profit / total_sales) * 100


# ============================================================
# NAVIGATION BUTTONS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home", use_container_width=True):
        home_page()
        st.rerun()

with col2:
    if st.button("⬅ Previous", use_container_width=True):
        previous_page()
        st.rerun()

with col3:
    if st.button("Next ➡", use_container_width=True):
        next_page()
        st.rerun()

with col4:
    if st.button("🔄 Next View", use_container_width=True):
        next_page()
        st.rerun()


st.markdown("---")


# ============================================================
# PAGE 0 - HOME
# ============================================================

if st.session_state.page == 0:

    st.title("📊 Sales Data Analysis Dashboard")

    st.subheader("Using Python, Pandas, NumPy, Matplotlib & Seaborn")

    st.write(
        """
        This project analyzes retail sales data to identify patterns
        in sales, profit, products, categories, regions, customers,
        and monthly performance.
        """
    )

    st.markdown("---")

    # KPI CARDS

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Sales",
        f"${total_sales:,.2f}"
    )

    col2.metric(
        "Total Profit",
        f"${total_profit:,.2f}"
    )

    col3.metric(
        "Total Quantity",
        f"{total_quantity:,}"
    )

    col4.metric(
        "Profit Margin",
        f"{profit_margin:.2f}%"
    )

    st.markdown("---")

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Project Workflow")

    st.write(
        """
        **Load Data → Inspect Data → Clean Data → Convert Dates →
        Group & Aggregate → Analyze → Visualize → Generate Insights**
        """
    )


# ============================================================
# PAGE 1 - SALES OVERVIEW
# ============================================================

elif st.session_state.page == 1:

    st.title("💰 Sales Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Sales", f"${total_sales:,.2f}")
    col2.metric("Total Profit", f"${total_profit:,.2f}")
    col3.metric("Average Sale", f"${average_sales:,.2f}")
    col4.metric("Quantity Sold", f"{total_quantity:,}")

    st.markdown("---")

    st.subheader("Sales by Category")

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.barplot(
        x=category_sales.index,
        y=category_sales.values,
        ax=ax
    )

    ax.set_xlabel("Category")
    ax.set_ylabel("Sales")
    ax.set_title("Total Sales by Category")

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Category Sales Data")

    st.dataframe(
        category_sales.reset_index(),
        use_container_width=True
    )


# ============================================================
# PAGE 2 - CATEGORY ANALYSIS
# ============================================================

elif st.session_state.page == 2:

    st.title("📦 Category Analysis")

    category_summary = (
        df.groupby("Category")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum"),
            Average_Discount=("Discount", "mean")
        )
        .sort_values("Sales", ascending=False)
    )

    st.subheader("Category Performance")

    st.dataframe(
        category_summary,
        use_container_width=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Sales by Category")

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.barplot(
            data=category_summary.reset_index(),
            x="Category",
            y="Sales",
            ax=ax
        )

        ax.set_title("Sales by Category")

        st.pyplot(fig)

    with col2:

        st.subheader("Profit by Category")

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.barplot(
            data=category_summary.reset_index(),
            x="Category",
            y="Profit",
            ax=ax
        )

        ax.set_title("Profit by Category")

        st.pyplot(fig)


# ============================================================
# PAGE 3 - REGIONAL ANALYSIS
# ============================================================

elif st.session_state.page == 3:

    st.title("🌎 Regional Analysis")

    region_summary = (
        df.groupby("Region")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
        .sort_values("Sales", ascending=False)
    )

    st.subheader("Regional Performance")

    st.dataframe(
        region_summary,
        use_container_width=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Sales by Region")

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.barplot(
            data=region_summary.reset_index(),
            x="Region",
            y="Sales",
            ax=ax
        )

        ax.set_title("Sales by Region")

        st.pyplot(fig)

    with col2:

        st.subheader("Profit by Region")

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.barplot(
            data=region_summary.reset_index(),
            x="Region",
            y="Profit",
            ax=ax
        )

        ax.set_title("Profit by Region")

        st.pyplot(fig)


# ============================================================
# PAGE 4 - PRODUCT ANALYSIS
# ============================================================

elif st.session_state.page == 4:

    st.title("🏆 Product Analysis")

    st.subheader("Top 10 Products by Sales")

    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(
        y=top_products.index,
        x=top_products.values,
        ax=ax
    )

    ax.set_xlabel("Sales")
    ax.set_ylabel("Product")
    ax.set_title("Top 10 Products by Sales")

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Top 10 Products Data")

    st.dataframe(
        top_products.reset_index(),
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Top 10 Products by Profit")

    top_profit_products = (
        df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.dataframe(
        top_profit_products.reset_index(),
        use_container_width=True
    )


# ============================================================
# PAGE 5 - MONTHLY TRENDS
# ============================================================

elif st.session_state.page == 5:

    st.title("📈 Monthly Sales Trends")

    monthly_sales = (
        df.groupby(
            df["Order Date"].dt.to_period("M")
        )["Sales"]
        .sum()
    )

    monthly_sales.index = monthly_sales.index.astype(str)

    st.subheader("Monthly Sales")

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        monthly_sales.index,
        monthly_sales.values,
        marker="o"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    ax.set_title("Monthly Sales Trend")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    st.pyplot(fig)

    st.markdown("---")

    highest_month = monthly_sales.idxmax()
    highest_month_sales = monthly_sales.max()

    st.success(
        f"Highest sales month: {highest_month} "
        f"with ${highest_month_sales:,.2f}"
    )

    st.subheader("Monthly Sales Data")

    st.dataframe(
        monthly_sales.reset_index(),
        use_container_width=True
    )


# ============================================================
# PAGE 6 - CUSTOMER & SHIPPING
# ============================================================

elif st.session_state.page == 6:

    st.title("👥 Customer & Shipping Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Sales by Customer Segment")

        segment_sales = (
            df.groupby("Segment")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.barplot(
            x=segment_sales.index,
            y=segment_sales.values,
            ax=ax
        )

        ax.set_title("Sales by Customer Segment")

        st.pyplot(fig)

    with col2:

        st.subheader("Sales by Ship Mode")

        ship_sales = (
            df.groupby("Ship Mode")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.barplot(
            x=ship_sales.index,
            y=ship_sales.values,
            ax=ax
        )

        ax.set_title("Sales by Ship Mode")

        plt.xticks(rotation=20)

        st.pyplot(fig)

    st.markdown("---")

    st.subheader("Segment Sales")

    st.dataframe(
        segment_sales.reset_index(),
        use_container_width=True
    )


# ============================================================
# PAGE 7 - CORRELATION ANALYSIS
# ============================================================

elif st.session_state.page == 7:

    st.title("🔍 Correlation Analysis")

    st.subheader("Sales vs Profit")

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="Sales",
        y="Profit",
        ax=ax
    )

    ax.set_title("Sales vs Profit")

    st.pyplot(fig)

    correlation = df["Sales"].corr(df["Profit"])

    st.metric(
        "Sales-Profit Correlation",
        f"{correlation:.4f}"
    )

    st.info(
        """
        Correlation measures the strength and direction of the
        relationship between two numerical variables.

        Correlation does not necessarily mean causation.
        """
    )

    st.markdown("---")

    st.subheader("Sales Distribution")

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.histplot(
        df["Sales"],
        bins=40,
        kde=True,
        ax=ax
    )

    ax.set_title("Distribution of Sales")

    st.pyplot(fig)

    st.markdown("---")

    st.subheader("Sales Outlier Analysis")

    fig, ax = plt.subplots(figsize=(10, 4))

    sns.boxplot(
        x=df["Sales"],
        ax=ax
    )

    ax.set_title("Sales Box Plot")

    st.pyplot(fig)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Sales Data Analysis | Python | Pandas | NumPy | Matplotlib | Seaborn | Streamlit"
)