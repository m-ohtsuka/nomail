-*- text -*-
=================================================================

  Nomail - ダイアルアップ・モバイル環境用オフライン SMTP サーバ

=================================================================

o お約束

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.


o はじめに

  Nomail はダイアルアップ・モバイル環境の為のオフラインメールサー
  バです。ローカル宛メールはそのまま配信しますが，自ホスト以外の
  メールは明示的に nosend を実行するまでキューに溜め続けるので，
  ネットワークが繋っていない状態でもメールを送ることができます。

  モバイル環境や，ダイアルアップ環境はもとより，メーラにオフライ
  ンモードが無く，Mew を使っていないのにわざわざ IM をインストー
  ルして imput でメールを送っているような方々にも特に便利に使っ
  ていただけると思います。

  また nomail は /usr/sbin/sendmail のふりをしますので，リンクを
  張ってもらえれば，そのまんま sendmail のように動きます。そんな
  わけで完全に sendmail を消してしまっても大丈夫です。


    IM の imput とどう違うの? (FAQ より)

    1. ローカル宛のメールを配送できます。
    2. SMTP でメールを送ることができます。
    3. インターネットへメールを出す際 Message-Id: を削除できます。
    4. 同様に From: のアドレスを書換えられます。
    5. エイリアスが使えます。
    6. 設定がすこぶる簡単です。

    7. news が送れません X)


o インストール

  同梱の INSTALL を良く読んでインストールしてください。実際に使
  うには perl (恐らく perl5.004 以上) と procmail が必要です。も
  しインストールされていなければ，あらかじめインストールしておい
  てください。（多くの Linux ディストリビューションは最初からイ
  ンストールされています）

  IPv6を用いた配送には、Socket6パッケージが必要です。お近くの
  CPANサイトから入手可能です。


o 使い方

  お好きなクライアントで SMTP サーバを Nomail の動いているホスト
  に向けてメールを出すだけです。直接 sendmail を起動するプログラ
  ムの場合は，/usr/sbin/sendmail の代りに nomail を呼び出すよう
  にしてください。 nomail から /usr/sbin/sendmail にリンクを張っ
  てもいいでしょう。

  ローカル宛メールはすぐに配信されます。インターネット宛のメール
  は nosend を実行するまでキュー(/var/nomail/) に溜められます。
  ネットワークに繋がったら nosend を実行しプロバイダの SMTP サー
  バに渡してください。


o エイリアス

   Nomail は sendmail の /etc/aliases をエミュレートすることがで
   きます。ただし | と include はサポートしていません。またメー
   ルはループしないようにしてください。Nomail 側ではチェックして
   いません。

   /etc/aliases は以下のような書式です。

   nobody:	root
   root:	negi
   negi:	hoge,huga,foo@bar.co.jp

   この例だと nobody 宛のメッセージは最終的に foo@bar.co.jp,
   hoge, huga, に送られます。


o 謝辞

   しまだみつのぶ <simm@KU3G.org> さんには多大な助言とコードをい
   ただきました。ありがとうございます。


o 作者

   御意見，御要望，バグ報告等ございましたら
   おおつかまさひと <negi@KU3G.org>
   まで御連絡ください。


o 最新版の配布

   http://www.KU3G.org/negi/nomail/
   ftp://ftp.KU3G.org/pub/nomail/
