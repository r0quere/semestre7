library IEEE;
use IEEE.std_logic_1164.all;

entity registre_tampon is
port( 	clk,reset,load	:	in std_logic;
	d_in 		: 	in std_logic_vector(7 downto 0);
	d_out 		: 	out std_logic_vector(7 downto 0));
end registre_tampon;

architecture arch_registre_tampon of registre_tampon is
begin
	process(clk,reset)
		begin
		if reset='1' then d_out <= (others => '0');
		elsif rising_edge(clk) then 
			if load='1' then d_out <= d_in;
			end if;
		end if;
	end process;
end arch_registre_tampon;

-------------------------------------------------------------------------------
library IEEE;
use IEEE.std_logic_1164.all;

entity registre_ctl is
port( 	clk,raz,load	:	in std_logic;
	d_in 		: 	in std_logic_vector(7 downto 0);
	d_out 		: 	out std_logic);
end registre_ctl;

architecture arch_registre_ctl of registre_ctl is
begin
	process(clk,raz)
		begin	
		if rising_edge(clk) then 
			if raz='1' then d_out <= '0';
			elsif load='1' then d_out <= d_in(0);
			end if;
		end if;
	end process;
end arch_registre_ctl;

-------------------------------------------------------------------------------
library IEEE;
use IEEE.std_logic_1164.all;

entity registre_etat is
port( 	clk,raz,set	:	in std_logic;
	d_out 		: 	out std_logic_vector(7 downto 0));
end registre_etat;

architecture arch_registre_etat of registre_etat is

begin
	process(clk)
		begin
		
		if rising_edge(clk) then 
			if raz='1' then d_out <= (others => '0');
			elsif set='1' then d_out(0) <= '1'; d_out(7 downto 1) <= (others => '0');
			end if;
		end if;
	end process;

end arch_registre_etat;

-------------------------------------------------------------------------------
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity compteur is
port( 	clk,raz,ce		:	in  std_logic;
	count 			: 	out std_logic_vector(3 downto 0));
end compteur;

architecture arch_compteur of compteur is
signal count_int : unsigned (3 downto 0);
begin
process(clk,raz)
	begin	
	if rising_edge(clk) then
		if raz='1' then count_int <= (others => '0');
		elsif ce='1' then			
			if count_int="1111" then count_int <= (others => '0'); -- fin de comptage
			else count_int <= count_int + 1; -- "+"(unsigned,int)
			end if;
		end if;
	end if;
end process;

count <= std_logic_vector(count_int); -- count copie de count_int

end arch_compteur;
-------------------------------------------------------------------------------
library IEEE;
use IEEE.std_logic_1164.all;

entity decodeur is
port(	E  :		in 	std_logic_vector(1 downto 0);
	S0,S1,S2 : 	out 	std_logic);
end decodeur;

architecture arch_decodeur of decodeur is
begin
	S0<='1' when E="00" else '0';
	S1<='1' when E="01" else '0';
	S2<='1' when E="10" else '0';
end arch_decodeur;
-------------------------------------------------------------------------------
library IEEE;
use IEEE.std_logic_1164.all;

entity detecteur_parite is
port(	E : in std_logic_vector( 7 downto 0);
	par : out std_logic);
end detecteur_parite;

architecture arch_detecteur_parite of detecteur_parite is
begin

par <= E(0) xor E(1) xor E(2) xor E(3) xor E(4) xor E(5) xor E(6) xor E(7);

end arch_detecteur_parite;
-------------------------------------------------------------------------------
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;


entity reg_serialisateur is
port( raz, clk, load, rotate : in std_logic;
	d_in : in std_logic_vector(8 downto 0);
	TX : out std_logic);
end reg_serialisateur;


architecture arch_reg_serialisateur of reg_serialisateur is
	signal internal_port : std_logic_vector(10 downto 0);
begin
	process(clk,raz)
		begin
		if rising_edge(clk) then 
			if raz='1' then internal_port<= "00000000001"; --reset data;
			end if;
			if rotate='1' then internal_port <= std_logic_vector(rotate_right(unsigned(internal_port),1));   
			end if;
			if load='1' then internal_port <= std_logic_vector(unsigned(d_in)&"01");
			end if;
		end if;
	end process;
	
	TX <= internal_port(0);


end arch_reg_serialisateur;



-------------------------------------------------------------------------------
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;


entity sequenceur_serial is
port( clk, reset, start,  ld_t: in std_logic;
	comptage : in std_logic_vector (3 downto 0);
	set_st, raz_st,raz_ctl, raz_ser, ld_ser, ser, raz_count, ce : out std_logic);
end sequenceur_serial;

architecture arch_sequenceur_serial of sequenceur_serial is
type etat_me is (E0,E1,E2,E3); --noms etats de notre machine
signal etat_cr, etat_sv : etat_me;
signal alreadyReset, alreadyLoad : std_logic;
begin
----------------------------------------------------------------------------------
process(clk,reset)  -- registre synchrone, maj etat_cr
begin
	if reset='1' then etat_cr <= E0; alreadyReset <= '0';
	elsif rising_edge(clk) then etat_cr <= etat_sv;
	end if;
end process;

----------------------------------------------------------------------------------  
process(start,ld_t,comptage,etat_cr)    -- process combinatoire
begin
	set_st <= '0';
	raz_st <= '1';
	raz_ctl <= '1';
	raz_ser <= '1';
	ld_ser <= '0';
	ser <= '0';
	--raz_count <= '1';
	ce <= '0';
	etat_sv <= etat_cr; -- sorties par defaut, on commence "proprement"
	
case etat_cr is
	when E0 => if ld_t='1' or alreadyLoad='1' then etat_sv <= E1; end if; -- maj etat_sv
		raz_ctl <= '1'; 
		raz_ser <= '1';
		raz_count <= '1';
		ld_ser <= '0'; 
		ser <= '0';  
		set_st <= '0'; 
		ce <= '0';
		if alreadyReset='0' then raz_st <= '1'; end if;
		alreadyReset <= '0';
	when E1 => if start = '1' then etat_sv <= E2; end if;
		alreadyLoad<='0';
		raz_st <= '0';
		raz_ctl <= '0'; 
		raz_ser <= '0';
		raz_count <= '0';
		set_st <= '1';
	when E2 => etat_sv <= E3; 
		raz_st <= '1';
		ld_ser <= '1';
		alreadyReset <= '1';
		if ld_t='1' then alreadyLoad <= '1'; end if;
	when E3 => if comptage = "1010" then etat_sv <= E0; end if;
		raz_st <= '0';
		ld_ser <= '0'; 
		ser <= '1';
		ce <= '1';
		if ld_t='1' then alreadyLoad <= '1'; end if;
end case;   
end process;
----------------------------------------------------------------------------------
end arch_sequenceur_serial;


-------------------------------------------------------------------------------
library IEEE;
use IEEE.std_logic_1164.all;
use work.all;

entity serial is
port( clk, reset : in std_logic;
	data : inout std_logic_vector(7 downto 0);
	address : in std_logic_vector(1 downto 0);
	tx : out std_logic);
end serial;


architecture arch_serial of serial is
signal ld_ctl,  raz_ser, start, oe_etat, set_st, raz_st, raz_ctl, ld_t, ld_ser, ser, par, ce, raz_count : std_logic;
signal comptage : std_logic_vector(3 downto 0);
signal etat : std_logic_vector(7 downto 0);
signal tamp_out : std_logic_vector(7 downto 0);
signal ser_in : std_logic_vector( 8 downto 0);

begin

data <= etat when oe_etat='1' else (others => 'Z');
ser_in <= par & tamp_out;

decod:		entity decodeur port map(
			E 		=> address,
			S0  		=> ld_ctl,
			S1		=> oe_etat,
			S2		=> ld_t
			);

tampon:		entity registre_tampon port map(
			clk		=> clk,
			reset		=> reset,
			load		=> ld_t,
			d_in 		=> data,
			d_out 		=> tamp_out
			);

ctl:		entity registre_ctl  port map(
			clk		=> clk,
			raz		=> raz_ctl,
			load		=> ld_ctl,
			d_in 		=> data,
			d_out 		=> start
			);


reg_etat:		entity registre_etat  port map(
			clk		=> clk,
			raz		=> raz_st,
			set		=> set_st,
			d_out 		=> etat
			);

seq:		entity sequenceur_serial port map(
			clk		=> clk,
			reset		=> reset,
			start		=> start,
			ld_t		=> ld_t,
			comptage 	=> comptage,
			set_st		=> set_st,
			raz_st		=> raz_st,
			raz_ctl		=> raz_ctl,
			raz_ser		=> raz_ser,
			ld_ser		=> ld_ser,
			ser		=> ser,
			raz_count	=> raz_count,
			ce 		=> ce
			);

compt:		entity compteur port map(
			clk		=> clk,
			raz		=> raz_count,
			ce		=> ce,
			count 		=> comptage
			);

detec_par:	entity detecteur_parite port map(
			E 		=> tamp_out,
			par		=> par
			);

reg_ser:	entity reg_serialisateur port map(
			raz		=> raz_ser,
			clk		=> clk,
			load		=> ld_ser,
			rotate		=> ser,
			d_in 		=> ser_in,
			TX		=> tx
			);

end arch_serial;