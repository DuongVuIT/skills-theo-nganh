#!/usr/bin/env python3
"""Tính các chỉ tiêu hiệu quả dự án: NPV, IRR, thời gian hoàn vốn, PI.

Ví dụ:
    python3 chi_tieu_du_an.py --rate 0.10 --cashflows -1000 200 300 400 500
"""
import argparse


def npv(rate, cashflows):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def irr(cashflows, lo=-0.99, hi=10.0, tol=1e-10, max_iter=1000):
    """Tìm IRR bằng phương pháp chia đôi; trả về None nếu không tìm được nghiệm."""
    f_lo, f_hi = npv(lo, cashflows), npv(hi, cashflows)
    if f_lo * f_hi > 0:
        return None
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        f_mid = npv(mid, cashflows)
        if abs(f_mid) < tol or (hi - lo) / 2 < tol:
            return mid
        if f_lo * f_mid < 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2


def payback(cashflows, rate=None):
    """Thời gian hoàn vốn (năm, có nội suy). rate != None thì tính có chiết khấu."""
    cumulative = 0.0
    for t, cf in enumerate(cashflows):
        value = cf if rate is None else cf / (1 + rate) ** t
        previous = cumulative
        cumulative += value
        if t > 0 and previous < 0 <= cumulative:
            return t - 1 + (-previous / value)
    return None


def sign_changes(cashflows):
    signs = [cf > 0 for cf in cashflows if cf != 0]
    return sum(1 for a, b in zip(signs, signs[1:]) if a != b)


def main():
    parser = argparse.ArgumentParser(description="Tính NPV, IRR, thời gian hoàn vốn, PI")
    parser.add_argument("--rate", type=float, required=True, help="Suất chiết khấu, ví dụ 0.1 cho 10%%")
    parser.add_argument("--cashflows", type=float, nargs="+", required=True,
                        help="Dòng tiền ròng từ năm 0, năm 0 thường là số âm")
    args = parser.parse_args()
    cfs = args.cashflows

    result_npv = npv(args.rate, cfs)
    result_irr = irr(cfs)
    pv_inflows = sum(cf / (1 + args.rate) ** t for t, cf in enumerate(cfs) if cf > 0)
    pv_outflows = -sum(cf / (1 + args.rate) ** t for t, cf in enumerate(cfs) if cf < 0)

    print(f"Suất chiết khấu: {args.rate:.2%}")
    print(f"NPV: {result_npv:,.2f}")
    print(f"IRR: {result_irr:.2%}" if result_irr is not None else "IRR: không xác định")
    if sign_changes(cfs) > 1:
        print("Cảnh báo: dòng tiền đổi dấu nhiều lần, có thể có nhiều IRR — nên dựa vào NPV.")
    simple = payback(cfs)
    discounted = payback(cfs, args.rate)
    print(f"Hoàn vốn giản đơn: {simple:.2f} năm" if simple is not None else "Hoàn vốn giản đơn: không hoàn vốn")
    print(f"Hoàn vốn có chiết khấu: {discounted:.2f} năm" if discounted is not None
          else "Hoàn vốn có chiết khấu: không hoàn vốn")
    print(f"PI (PV thu / PV chi): {pv_inflows / pv_outflows:.3f}" if pv_outflows else "PI: không xác định")


if __name__ == "__main__":
    main()
