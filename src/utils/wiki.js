import MD5 from "md5";

export const TORAPPU_ENDPOINT = "https://torappu.prts.wiki";
export const STATIC_ENDPOINT = "https://static.prts.wiki";
export const PRTS_BASE_DOMAIN = "https://prts.wiki";
export const KEY_STRING =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+,";
export const MEDIA_ENDPOINT = "https://media.prts.wiki";
export const WEEDY_ENDPOINT = "https://weedy.prts.wiki";


export const charListData = {
  uhs: `${MEDIA_ENDPOINT}/7/7f/干员图鉴_uh_阴影.png`,
  lh: (r) => {
    const _lh = [
      "0/0b/干员图鉴_lh_0%2C1%2C2.png",
      "a/a5/干员图鉴_lh_3.png",
      "9/9e/干员图鉴_lh_4.png",
      "a/a5/干员图鉴_lh_5.png",
    ];
    return `${MEDIA_ENDPOINT}/${r < 3 ? _lh[0] : _lh[r - 2]}`;
  },
  bg: (r) => {
    const _bg = [
      "2/25/干员图鉴_背景_0%2C1%2C2.png",
      "b/b1/干员图鉴_背景_3.png",
      "a/ad/干员图鉴_背景_4.png",
      "c/c9/干员图鉴_背景_5.png",
    ];
    return `${MEDIA_ENDPOINT}/${r < 3 ? _bg[0] : _bg[r - 2]}`;
  },
  patch: `${MEDIA_ENDPOINT}/2/20/干员图鉴_补丁.png`,
};

export function getImagePath(filename) {
  const md5 = MD5(filename);
  return `${MEDIA_ENDPOINT}/${md5.slice(0, 1)}/${md5.slice(0, 2)}/${filename}`;
}

export const professionMap = {
  PIONEER: "先锋",
  WARRIOR: "近卫",
  SNIPER: "狙击",
  SUPPORT: "辅助",
  CASTER: "术师",
  SPECIAL: "特种",
  MEDIC: "医疗",
  TANK: "重装",
};
